"""empty message

Revision ID: 962b1609f27e
Revises: ad29cc6bd826
Create Date: 2022-09-16 14:07:44.976626

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '962b1609f27e'
down_revision = 'ad29cc6bd826'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('access_token', sa.String(length=120), nullable=True))
    op.alter_column('users', 'remember_token',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'remember_token',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.drop_column('users', 'access_token')
    # ### end Alembic commands ###
