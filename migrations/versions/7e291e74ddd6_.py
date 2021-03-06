"""empty message

Revision ID: 7e291e74ddd6
Revises: 7dc9eb9eec3c
Create Date: 2022-06-01 00:06:04.091410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e291e74ddd6'
down_revision = '7dc9eb9eec3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_temp_table_index', table_name='temp_table')
    op.drop_table('temp_table')
    op.alter_column('products', 'article',
               existing_type=sa.TEXT(),
               nullable=False)
    op.create_foreign_key(None, 'products', 'companies', ['company_id'], ['id'])
    op.add_column('users', sa.Column('role', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.alter_column('products', 'article',
               existing_type=sa.TEXT(),
               nullable=True)
    op.create_table('temp_table',
    sa.Column('index', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('company_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('article', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('net_cost', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_temp_table_index', 'temp_table', ['index'], unique=False)
    # ### end Alembic commands ###
