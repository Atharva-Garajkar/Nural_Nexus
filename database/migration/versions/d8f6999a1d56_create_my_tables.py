"""create_my_tables

Revision ID: d8f6999a1d56
Revises: fd315e212f8d
Create Date: 2024-11-20 12:55:11.985760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8f6999a1d56'
down_revision: Union[str, None] = 'fd315e212f8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
