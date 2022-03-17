"""add default users

Revision ID: fb03046e541d
Revises: ca5ef0a39e14
Create Date: 2022-03-16 23:49:16.812323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from passlib.context import CryptContext
from sqlalchemy import table, insert, Table, MetaData

revision = 'fb03046e541d'
down_revision = 'ca5ef0a39e14'
branch_labels = None
depends_on = None

metadata = MetaData()


def upgrade():
    user_table = Table('auth_user', metadata,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )

    for i in range(1, 4):
        try:
            op.execute(user_table.insert().values(
                username=f'user{i}',
                password=CryptContext(schemes=['sha256_crypt']).hash('123'))
            )
        except:
            pass


def downgrade():
    pass
