"""empty message

Revision ID: 292d0ae7ab06
Revises: 
Create Date: 2022-02-02 10:31:42.158584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '292d0ae7ab06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'create_dttm')
    op.drop_column('category', 'update_dttm')
    op.drop_column('film_actor', 'create_dttm')
    op.drop_column('film_actor', 'update_dttm')
    op.drop_column('film_category', 'create_dttm')
    op.drop_column('film_category', 'update_dttm')
    op.drop_column('language', 'create_dttm')
    op.drop_column('language', 'update_dttm')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('language', sa.Column('update_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('language', sa.Column('create_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('film_category', sa.Column('update_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('film_category', sa.Column('create_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('film_actor', sa.Column('update_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('film_actor', sa.Column('create_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('category', sa.Column('update_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    op.add_column('category', sa.Column('create_dttm', sa.VARCHAR(length=256), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
