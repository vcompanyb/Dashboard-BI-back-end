"""empty message

Revision ID: c854d1b2c3cd
Revises: bad4e6a6da55
Create Date: 2020-07-07 11:14:08.209016

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c854d1b2c3cd'
down_revision = 'bad4e6a6da55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enterprise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('CIF_number', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('CIF_number'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('platform',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('logo', sa.String(length=120), nullable=True),
    sa.Column('enterprise_to_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enterprise_to_id'], ['enterprise.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('integration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('API_key', sa.String(length=120), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('platform_id', sa.Integer(), nullable=True),
    sa.Column('brand_to_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_to_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('midata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('detail', sa.String(length=250), nullable=True),
    sa.Column('brand_to_id', sa.Integer(), nullable=True),
    sa.Column('integration_to_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_to_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['integration_to_id'], ['integration.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`is_active` in (0,1))', name='user_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_table('midata')
    op.drop_table('integration')
    op.drop_table('brand')
    op.drop_table('platform')
    op.drop_table('enterprise')
    # ### end Alembic commands ###