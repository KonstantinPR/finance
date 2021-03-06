"""empty message

Revision ID: 69ac01c66d75
Revises: bf8bad0ed054
Create Date: 2022-06-09 16:54:31.979913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69ac01c66d75'
down_revision = 'bf8bad0ed054'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('executor_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'users', ['executor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'executor_id')
    # ### end Alembic commands ###
