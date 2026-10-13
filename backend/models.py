from datetime import date, time
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    
class Workout(Base):
    __tablename__ = "workouts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    workout_date: Mapped[date] = mapped_column()
    workout_time: Mapped[time] = mapped_column()
    workout_type: Mapped[str | None] = mapped_column(String(255))
    
class Exercise(Base):
    __tablename__ = "exercises"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(255))
    
class WorkoutSet(Base):
    __tablename__ = "sets"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    workout_id: Mapped[int] = mapped_column(ForeignKey("workouts.id"))
    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id"))
    weight: Mapped[float] = mapped_column()
    reps: Mapped[int] = mapped_column()
    reps_in_reserve: Mapped[int | None] = mapped_column()