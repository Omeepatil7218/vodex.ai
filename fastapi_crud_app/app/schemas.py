from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime  # DateTime parsing

class ItemUpdate(BaseModel):
    name: str = None
    email: str = None
    item_name: str = None
    quantity: int = None
    expiry_date: datetime = None

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInUpdate(BaseModel):
    email: str = None
    location: str = None
