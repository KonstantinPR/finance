"""empty message

Revision ID: df66fdc7bb9d
Revises: 69ac01c66d75
Create Date: 2022-06-09 17:22:56.054302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df66fdc7bb9d'
down_revision = '69ac01c66d75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
