"""empty message

Revision ID: 9f0737dc10ec
Revises: 4cd60c0dd727
Create Date: 2023-02-23 18:22:59.763310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f0737dc10ec'
down_revision = '4cd60c0dd727'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bio', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('bio')

    # ### end Alembic commands ###
