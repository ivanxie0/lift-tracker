"""Seed muscles

Revision ID: 328b8500f196
Revises: ca3421a0eddb
Create Date: 2026-10-23 01:50:49.764086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '328b8500f196'
down_revision: Union[str, Sequence[str], None] = 'ca3421a0eddb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    muscles = sa.table(
        "muscles",
        sa.column("name", sa.String),
        sa.column("muscle_group", sa.String),
    )
    op.bulk_insert(muscles, [
        # Chest
        {"name": "Upper Chest", "muscle_group": "Chest"},
        {"name": "Mid Chest", "muscle_group": "Chest"},
        {"name": "Lower Chest", "muscle_group": "Chest"},
        {"name": "Serratus Anterior", "muscle_group": "Chest"},
        # Back
        {"name": "Lats", "muscle_group": "Back"},
        {"name": "Upper Back / Traps", "muscle_group": "Back"},
        {"name": "Rhomboids", "muscle_group": "Back"},
        {"name": "Lower Back", "muscle_group": "Back"},
        # Shoulders
        {"name": "Front Delt", "muscle_group": "Shoulders"},
        {"name": "Side Delt", "muscle_group": "Shoulders"},
        {"name": "Rear Delt", "muscle_group": "Shoulders"},
        {"name": "Rotator Cuff", "muscle_group": "Shoulders"},
        # Arms
        {"name": "Biceps", "muscle_group": "Arms"},
        {"name": "Brachialis", "muscle_group": "Arms"},
        {"name": "Triceps", "muscle_group": "Arms"},
        {"name": "Forearms", "muscle_group": "Arms"},
        # Legs
        {"name": "Quadriceps", "muscle_group": "Legs"},
        {"name": "Hamstrings", "muscle_group": "Legs"},
        {"name": "Glutes", "muscle_group": "Legs"},
        {"name": "Calves", "muscle_group": "Legs"},
        {"name": "Adductors", "muscle_group": "Legs"},
        {"name": "Abductors", "muscle_group": "Legs"},
        {"name": "Hip Flexors", "muscle_group": "Legs"},
        # Core
        {"name": "Abs", "muscle_group": "Core"},
        {"name": "Obliques", "muscle_group": "Core"},
    ])


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM muscles")
