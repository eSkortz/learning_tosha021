"""create_my_table

Revision ID: d4ad614c851a
Revises: 
Create Date: 2024-02-11 20:03:46.111978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd4ad614c851a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('surname', sa.TEXT(), nullable=False),
    sa.Column('phone', sa.INTEGER(), nullable=False),
    sa.Column('birthday', postgresql.TIMESTAMP(), nullable=False),
    sa.Column('lastname', sa.TEXT(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_users_id'), 'users', ['id'], unique=False, schema='public')
    op.create_table('users_copy',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('surname', sa.TEXT(), nullable=False),
    sa.Column('phone', sa.INTEGER(), nullable=False),
    sa.Column('birthday', postgresql.TIMESTAMP(), nullable=False),
    sa.Column('lastname', sa.TEXT(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    op.create_index(op.f('ix_public_users_copy_id'), 'users_copy', ['id'], unique=False, schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_public_users_copy_id'), table_name='users_copy', schema='public')
    op.drop_table('users_copy', schema='public')
    op.drop_index(op.f('ix_public_users_id'), table_name='users', schema='public')
    op.drop_table('users', schema='public')
    # ### end Alembic commands ###
