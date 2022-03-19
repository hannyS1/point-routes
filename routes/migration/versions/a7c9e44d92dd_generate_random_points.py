"""generate random points

Revision ID: a7c9e44d92dd
Revises: 0ebd05860f46
Create Date: 2022-03-20 01:23:02.999683

"""
import random

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Table, MetaData

revision = 'a7c9e44d92dd'
down_revision = '0ebd05860f46'
branch_labels = None
depends_on = None

metadata = MetaData()


def upgrade():

    def generate_random_coordinates() -> (float, float):
        latitude = random.randint(1, 100) + round(random.random(), 3)
        longitude = random.randint(1, 100) + round(random.random(), 3)
        return latitude, longitude

    def generate_points(count: int):
        points = []
        for i in range(count):
            coordinates = generate_random_coordinates()
            point = {
                'latitude': coordinates[0],
                'longitude': coordinates[1],
                'title': f'test_point_title_{i}',
                'deleted': False
            }
            points.append(point)

        return points

    point_table = Table('point', metadata,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('latitude', sa.Float(), nullable=False),
        sa.Column('longitude', sa.Float(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    points = generate_points(10000)
    query = point_table.insert().values(points)
    op.execute(query)


def downgrade():
    pass
