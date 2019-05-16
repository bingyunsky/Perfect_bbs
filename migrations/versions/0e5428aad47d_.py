"""empty message

Revision ID: 0e5428aad47d
Revises: 4020a8bfb725
Create Date: 2019-05-16 14:20:18.482125

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0e5428aad47d'
down_revision = '4020a8bfb725'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('_password', sa.String(length=100), nullable=False))
    op.drop_column('cms_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('cms_user', '_password')
    # ### end Alembic commands ###
