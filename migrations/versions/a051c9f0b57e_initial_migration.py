"""initial migration

Revision ID: a051c9f0b57e
Revises: 
Create Date: 2025-02-17 21:44:41.974481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a051c9f0b57e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('theme', sa.String(length=10), nullable=True),
    sa.Column('embedding_vector', sa.PickleType(), nullable=True),
    sa.Column('unlocked_themes', sa.String(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('dashboard_layout', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('read_article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('article_title', sa.String(length=500), nullable=True),
    sa.Column('article_url', sa.String(length=500), nullable=False),
    sa.Column('read_at', sa.DateTime(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('interaction_strength', sa.Float(), nullable=True),
    sa.Column('bookmarked', sa.Boolean(), nullable=True),
    sa.Column('source', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('search_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('query', sa.String(length=100), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search_history')
    op.drop_table('read_article')
    op.drop_table('user')
    # ### end Alembic commands ###
