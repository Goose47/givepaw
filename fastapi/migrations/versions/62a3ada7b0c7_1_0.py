"""1.0

Revision ID: 62a3ada7b0c7
Revises: 
Create Date: 2024-02-23 19:21:13.076172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62a3ada7b0c7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pet_types', sa.Column('icon', sa.String(), nullable=False))
    op.alter_column('users', 'avatar_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'avatar_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('pet_types', 'icon')
    # ### end Alembic commands ###