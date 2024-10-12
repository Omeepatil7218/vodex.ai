from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    expiry_date: Optional[datetime] = None
