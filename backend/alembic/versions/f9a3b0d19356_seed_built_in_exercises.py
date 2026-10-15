"""Seed built-in exercises

Revision ID: f9a3b0d19356
Revises: 79fb0032ec9d
Create Date: 2026-10-14 23:09:04.780786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9a3b0d19356'
down_revision: Union[str, Sequence[str], None] = '79fb0032ec9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    exercises = sa.table("exercises", sa.column("name", sa.String))
    op.bulk_insert(exercises, [
        {"name": "Bench Press"},
        {"name": "Incline Dumbbell Press"},
        {"name": "Chest Dip"},
        {"name": "Barbell Row"},
        {"name": "Seated Cable Row"},
        {"name": "Pendlay Row"},
        {"name": "Pull-Up"},
        {"name": "Lat Pulldown"},
        {"name": "Overhead Press"},
        {"name": "Seated Dumbbell Shoulder Press"},
        {"name": "Dumbbell Lateral Raise"},
        {"name": "Face Pull"},
        {"name": "Dumbbell Shrug"},
        {"name": "Squat"},
        {"name": "Leg Press"},
        {"name": "Hack Squat"},
        {"name": "Bulgarian Split Squat"},
        {"name": "Barbell Hip Thrust"},
        {"name": "Deadlift"},
        {"name": "Romanian Deadlift"},
        {"name": "Leg Curl"},
        {"name": "Leg Extension"},
        {"name": "Standing Calf Raise"},
        {"name": "Barbell Bicep Curl"},
        {"name": "Barbell Preacher Curl"},
        {"name": "Triceps Pushdown"},
        {"name": "Skull Crusher"},
        {"name": "Overhead Triceps Extension"},
        {"name": "Hanging Leg Raise"},
        {"name": "Standing Cable Woodchopper"}
    ])

def downgrade() -> None:
    op.execute("DELETE FROM exercises WHERE user_id is NULL")
