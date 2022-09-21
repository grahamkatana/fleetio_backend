"""empty message

Revision ID: 8636ba790352
Revises: a8cbd4a2ec3a
Create Date: 2022-09-21 18:23:21.758393

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8636ba790352'
down_revision = 'a8cbd4a2ec3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('company_type', sa.String(length=20), nullable=True))
    op.add_column('ondemands', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('ondemands', sa.Column('expires_at', sa.DateTime(), nullable=False))
    op.drop_constraint('transporttypes_ibfk_1', 'transporttypes', type_='foreignkey')
    op.drop_column('transporttypes', 'company_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transporttypes', sa.Column('company_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True))
    op.create_foreign_key('transporttypes_ibfk_1', 'transporttypes', 'companies', ['company_id'], ['id'])
    op.drop_column('ondemands', 'expires_at')
    op.drop_column('ondemands', 'is_active')
    op.drop_column('companies', 'company_type')
    # ### end Alembic commands ###
