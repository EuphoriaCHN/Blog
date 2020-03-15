"""normal

Revision ID: 188c5acedf43
Revises: 434bd6f80699
Create Date: 2020-03-10 15:55:02.668127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '188c5acedf43'
down_revision = '434bd6f80699'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_followeds_posts_read_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('last_follows_read_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('last_likes_read_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('last_likes_read_time')
        batch_op.drop_column('last_follows_read_time')
        batch_op.drop_column('last_followeds_posts_read_time')

    # ### end Alembic commands ###
