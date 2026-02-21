"""Add token scopes

Revision ID: 7265c4fdf605
Revises: 0ba45693748d
Create Date: 2026-02-21 00:00:00.000000

"""

revision = '7265c4fdf605'
down_revision = '0ba45693748d'

from alembic import op
import sqlalchemy as sa
import mailu


def upgrade():
    op.add_column('token', sa.Column('scopes', mailu.models.CommaSeparatedList(), nullable=True))


def downgrade():
    op.drop_column('token', 'scopes')
