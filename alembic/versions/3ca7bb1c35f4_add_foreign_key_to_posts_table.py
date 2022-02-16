"""add foreign-key to posts table

Revision ID: 3ca7bb1c35f4
Revises: 07d9cd1a8ace
Create Date: 2022-02-11 13:31:31.790053

"""
# from tkinter import CASCADE
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ca7bb1c35f4'
down_revision = '07d9cd1a8ace'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
