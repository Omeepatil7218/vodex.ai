from pydantic import BaseModel
from bson import ObjectId

class Item(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: str  # ISO format date string
    insert_date: str  # ISO format date string

    class Config:
        # Allow ObjectId to be serialized to string
        json_encoders = {
            ObjectId: str
        }

class ClockInRecord(BaseModel):
    email: str
    location: str
    insert_datetime: str  # ISO format datetime string

    class Config:
        # Allow ObjectId to be serialized to string
        json_encoders = {
            ObjectId: str
        }
