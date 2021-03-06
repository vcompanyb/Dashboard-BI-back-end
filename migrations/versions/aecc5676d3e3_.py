"""empty message

Revision ID: aecc5676d3e3
Revises: e02e13503dba
Create Date: 2020-07-13 16:48:10.595514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aecc5676d3e3'
down_revision = 'e02e13503dba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('integration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('API_key', sa.String(length=120), nullable=True),
    sa.Column('brand_to_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_to_id'], ['brand.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('integration')
    # ### end Alembic commands ###
