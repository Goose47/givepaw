"""empty message

Revision ID: ad64b760f1c6
Revises: 97a5b04488a1
Create Date: 2024-02-24 15:07:32.460347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad64b760f1c6'
down_revision: Union[str, None] = '97a5b04488a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('avatars', 'photo_thumb',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('blood_components', 'icon',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pet_types', 'icon',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pets', 'breed_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pets', 'breed',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pets', 'avatar_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'patronymic',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'patronymic',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pets', 'avatar_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pets', 'breed',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pets', 'breed_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pet_types', 'icon',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('blood_components', 'icon',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('avatars', 'photo_thumb',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
