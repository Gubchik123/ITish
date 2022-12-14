"""Add 'title' for Tag model

Revision ID: 5412d161642d
Revises: 
Create Date: 2022-11-20 11:08:36.975107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5412d161642d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('title', sa.String(length=30), nullable=False))
    op.create_unique_constraint(None, 'tags', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tags', type_='unique')
    op.drop_column('tags', 'title')
    # ### end Alembic commands ###
