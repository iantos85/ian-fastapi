"""add content column to posts table

Revision ID: 17efe6f33792
Revises: bd0a7c2a36a8
Create Date: 2022-02-11 13:05:19.518621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17efe6f33792'
down_revision = 'bd0a7c2a36a8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
