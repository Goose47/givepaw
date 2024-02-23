"""empty message

Revision ID: 1ab0c2771225
Revises: aefe0d34a61c
Create Date: 2024-02-23 18:40:56.044957

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ab0c2771225'
down_revision: Union[str, None] = 'aefe0d34a61c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
