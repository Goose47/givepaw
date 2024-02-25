"""empty message

Revision ID: 71a45c75a78c
Revises: 84aac2f182f6
Create Date: 2024-02-25 04:53:31.989999

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71a45c75a78c'
down_revision: Union[str, None] = '84aac2f182f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donors__bloods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('donor_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('blood_amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinics.id'], ),
    sa.ForeignKeyConstraint(['donor_id'], ['donors.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['recipient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('donors', sa.Column('clinic_id', sa.Integer(), nullable=False))
    op.add_column('donors', sa.Column('date', sa.Date(), nullable=False))
    op.drop_constraint('donors_city_id_fkey', 'donors', type_='foreignkey')
    op.create_foreign_key(None, 'donors', 'clinics', ['clinic_id'], ['id'])
    op.drop_column('donors', 'city_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donors', sa.Column('city_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'donors', type_='foreignkey')
    op.create_foreign_key('donors_city_id_fkey', 'donors', 'cities', ['city_id'], ['id'])
    op.drop_column('donors', 'date')
    op.drop_column('donors', 'clinic_id')
    op.drop_table('donors__bloods')
    # ### end Alembic commands ###
