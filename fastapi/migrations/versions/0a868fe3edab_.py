"""empty message

Revision ID: 0a868fe3edab
Revises: 4c119044593b
Create Date: 2024-02-24 20:48:37.704634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a868fe3edab'
down_revision: Union[str, None] = '4c119044593b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donors', sa.Column('recipient_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'donors', 'recipient', ['recipient_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'donors', type_='foreignkey')
    op.drop_column('donors', 'recipient_id')
    # ### end Alembic commands ###