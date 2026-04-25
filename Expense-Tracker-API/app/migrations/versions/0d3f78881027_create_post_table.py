"""create post table

Revision ID: 0d3f78881027
Revises: 6d3d90ce93f2
Create Date: 2026-04-25 03:45:10.593929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d3f78881027'
down_revision: Union[str, Sequence[str], None] = '6d3d90ce93f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
    CREATE TABLE IF NOT EXISTS post(
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        categories VARCHAR(255) NOT NULL,
        amount NUMERIC(15, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        update_at TIMESTAMP DEFAULT NULL
    );
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TABLE IF EXISTS post")
