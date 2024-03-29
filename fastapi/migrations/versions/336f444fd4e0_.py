"""empty message

Revision ID: 336f444fd4e0
Revises: 584a0e0439e5
Create Date: 2024-02-25 05:27:03.899170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '336f444fd4e0'
down_revision: Union[str, None] = '584a0e0439e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_clinics_address', table_name='clinics')
    op.create_index(op.f('ix_clinics_address'), 'clinics', ['address'], unique=False)
    op.drop_index('ix_clinics_email', table_name='clinics')
    op.create_index(op.f('ix_clinics_email'), 'clinics', ['email'], unique=False)
    op.drop_index('ix_clinics_phone', table_name='clinics')
    op.create_index(op.f('ix_clinics_phone'), 'clinics', ['phone'], unique=False)
    op.drop_index('ix_clinics_title', table_name='clinics')
    op.create_index(op.f('ix_clinics_title'), 'clinics', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_clinics_title'), table_name='clinics')
    op.create_index('ix_clinics_title', 'clinics', ['title'], unique=True)
    op.drop_index(op.f('ix_clinics_phone'), table_name='clinics')
    op.create_index('ix_clinics_phone', 'clinics', ['phone'], unique=True)
    op.drop_index(op.f('ix_clinics_email'), table_name='clinics')
    op.create_index('ix_clinics_email', 'clinics', ['email'], unique=True)
    op.drop_index(op.f('ix_clinics_address'), table_name='clinics')
    op.create_index('ix_clinics_address', 'clinics', ['address'], unique=True)
    # ### end Alembic commands ###
