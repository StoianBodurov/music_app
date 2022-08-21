from werkzeug.exceptions import NotFound

from db import db


def delete_item(item_model, pk):
    try:
        model = item_model()
        item = model.query.filter_by(id=pk).first()
        db.session.delete(item)
        db.session.flush()
    except Exception:
        raise NotFound('Item not exist')


def update_item(item_model, data, pk):
    model = item_model()
    item = model.query.filter_by(id=pk).first()
    if not item:
        raise NotFound('Item not exist')
    try:
        model.query.filter_by(id=pk).update(data)
        db.session.flush()
        return item
    except Exception as ex:
        raise Exception(str(ex))


def get_item(item_model, pk):
    model = item_model()
    return model.query.filter_by(id=pk).first()

