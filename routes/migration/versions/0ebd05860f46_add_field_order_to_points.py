"""add field order to points

Revision ID: 0ebd05860f46
Revises: 5c3a5e03ca73
Create Date: 2022-03-18 18:18:58.483643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ebd05860f46'
down_revision = '5c3a5e03ca73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('routes_points', sa.Column('order', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('routes_points', 'order')
    # ### end Alembic commands ###
