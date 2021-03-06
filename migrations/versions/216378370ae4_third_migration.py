"""Third Migration

Revision ID: 216378370ae4
Revises: f31dd5cdc81d
Create Date: 2019-02-19 05:51:40.716914

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '216378370ae4'
down_revision = 'f31dd5cdc81d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('date_posted', sa.String(), nullable=True))
    op.add_column('blogs', sa.Column('description', sa.String(), nullable=False))
    op.add_column('blogs', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('title', sa.String(), nullable=True))
    op.create_index(op.f('ix_blogs_description'), 'blogs', ['description'], unique=False)
    op.drop_constraint('blogs_user_id_fkey', 'blogs', type_='foreignkey')
    op.create_foreign_key(None, 'blogs', 'users', ['owner_id'], ['id'])
    op.drop_column('blogs', 'posted')
    op.drop_column('blogs', 'blog_title')
    op.drop_column('blogs', 'blog_content')
    op.drop_column('blogs', 'user_id')
    op.drop_column('blogs', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('category', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('blogs', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('blog_content', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('blog_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.create_foreign_key('blogs_user_id_fkey', 'blogs', 'users', ['user_id'], ['id'])
    op.drop_index(op.f('ix_blogs_description'), table_name='blogs')
    op.drop_column('blogs', 'title')
    op.drop_column('blogs', 'owner_id')
    op.drop_column('blogs', 'description')
    op.drop_column('blogs', 'date_posted')
    # ### end Alembic commands ###
