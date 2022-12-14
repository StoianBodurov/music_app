"""add role column in user model

Revision ID: 0a6aedd49592
Revises: eff1224db90c
Create Date: 2022-08-19 16:14:05.703504

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0a6aedd49592'
down_revision = 'eff1224db90c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    userrolesenum = postgresql.ENUM('admin', 'user', name='userrolesenum')
    userrolesenum.create(op.get_bind())
    op.add_column('users', sa.Column('role', sa.Enum('user', 'admin', name='userrolesenum'), server_default='user', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
