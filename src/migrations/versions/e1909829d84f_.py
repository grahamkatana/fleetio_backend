"""empty message

Revision ID: e1909829d84f
Revises: 46c814dca8b2
Create Date: 2022-09-16 12:28:26.204730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1909829d84f'
down_revision = '46c814dca8b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permittypes',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('is_local', sa.Boolean(), nullable=False),
    sa.Column('company_id', sa.BigInteger(), nullable=True),
    sa.Column('regions', sa.String(length=300), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transporttypes',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('company_id', sa.BigInteger(), nullable=True),
    sa.Column('type', sa.String(length=300), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('companies', sa.Column('country', sa.String(length=80), nullable=True))
    op.add_column('fleets', sa.Column('permit_type_id', sa.BigInteger(), nullable=True))
    op.add_column('fleets', sa.Column('transport_type_id', sa.BigInteger(), nullable=True))
    op.create_foreign_key(None, 'fleets', 'permittypes', ['permit_type_id'], ['id'])
    op.create_foreign_key(None, 'fleets', 'transporttypes', ['transport_type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fleets', type_='foreignkey')
    op.drop_constraint(None, 'fleets', type_='foreignkey')
    op.drop_column('fleets', 'transport_type_id')
    op.drop_column('fleets', 'permit_type_id')
    op.drop_column('companies', 'country')
    op.drop_table('transporttypes')
    op.drop_table('permittypes')
    # ### end Alembic commands ###
