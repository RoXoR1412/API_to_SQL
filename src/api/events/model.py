from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime

class Steps(SQLModel, table=True,table_name="Steps"):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    steps: int
    distance_km: float
    calories_burned: float
    active_minutes: int
    sleep_hours: float
    water_intake_liters: float
    mood: str
    