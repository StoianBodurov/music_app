import json

from flask_testing import TestCase

from config import create_app
from db import db
from tests.base import generate_token
from utils.factories import UserFactory


class TestApp(TestCase):
    def create_app(self):
        return create_app('config.TestingConfig')

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_protected(self):
        for method, url in [
            ('GET', '/user'),
            ('POST', '/album/create'),
            ('PUT', '/album/1'),
            ('DELETE', '/album/1'),
            ('POST', '/album/1/songs/create'),
            ('PUT', '/songs/1'),
            ('DELETE', '/songs/1'),
        ]:
            if method == 'POST':
                response = self.client.post(url, data=json.dumps({}))
            elif method == 'GET':
                response = self.client.get(url)
            elif method == 'PUT':
                response = self.client.put(url, data=json.dumps({}))
            else:
                response = self.client.delete(url)

            self.assert_401(response, {'message': 'Invalid or missing token'})

    def test_protected_admin_required_admin_rights(self):
        url = '/admin/create'
        user = UserFactory()
        token = generate_token(user)
        headers = {'Authorization': f'Bearer {token}'}
        response = self.client.post(url, data=json.dumps({}), headers=headers)
        self.assert403(response, {'message': 'You do not have the rights to access this resource'})
