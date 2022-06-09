"""empty message

Revision ID: 1a815d8df732
Revises: 1263de9d6d43
Create Date: 2022-06-09 22:09:06.340482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a815d8df732'
down_revision = '1263de9d6d43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('points', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'points')
    # ### end Alembic commands ###
