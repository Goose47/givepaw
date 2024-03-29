"""empty message

Revision ID: e5ba4b2c95e2
Revises: 2cf80b1b11cd
Create Date: 2024-02-25 05:03:00.007878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5ba4b2c95e2'
down_revision: Union[str, None] = '2cf80b1b11cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('donors_clinic_id_fkey', 'donors', type_='foreignkey')
    op.drop_column('donors', 'date')
    op.drop_column('donors', 'clinic_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donors', sa.Column('clinic_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('donors', sa.Column('date', sa.DATE(), autoincrement=False, nullable=False))
    op.create_foreign_key('donors_clinic_id_fkey', 'donors', 'clinics', ['clinic_id'], ['id'])
    # ### end Alembic commands ###
