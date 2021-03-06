"""create point table

Revision ID: 9260266d067e
Revises: fb47e19380d1
Create Date: 2022-03-17 15:30:44.417687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9260266d067e'
down_revision = 'fb47e19380d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routes_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routes_point')
    # ### end Alembic commands ###
