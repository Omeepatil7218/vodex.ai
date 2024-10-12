from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInUpdate(BaseModel):
    email: Optional[str] = None
    location: Optional[str] = None
