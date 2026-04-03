"""create posts table

Revision ID: d48e1b64469b
Revises: f07dc92fa3e2
Create Date: 2026-03-30 14:47:37.391282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd48e1b64469b'
down_revision: Union[str, Sequence[str], None] = 'f07dc92fa3e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        CREATE TABLE IF NOT EXISTS posts(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NULL);
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TABLE IF EXISTS posts")
