from fastapi import APIRouter, HTTPException
from app.schemas import ClockInCreate
from app.database import mongo_db
import datetime
from bson import ObjectId

router = APIRouter()

@router.post("/clock-in")
async def create_clock_in(clock_in: ClockInCreate):
    try:
        clock_in_data = clock_in.dict()
        clock_in_data["insert_datetime"] = datetime.datetime.now()
        result = await mongo_db.clock_in_collection.insert_one(clock_in_data)
        clock_in_data["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return clock_in_data
    except Exception as e:
        print(f"Error occurred while creating clock-in record: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/clock-in/{clock_in_id}")
async def get_clock_in(clock_in_id: str):
    try:
        clock_in = await mongo_db.clock_in_collection.find_one({"_id": ObjectId(clock_in_id)})
        if clock_in:
            clock_in["_id"] = str(clock_in["_id"])  # Convert ObjectId to string
            return clock_in
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    except Exception as e:
        print(f"Error occurred while retrieving clock-in record: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/clock-in/{clock_in_id}")
async def delete_clock_in(clock_in_id: str):
    try:
        result = await mongo_db.clock_in_collection.delete_one({"_id": ObjectId(clock_in_id)})
        if result.deleted_count == 1:
            return {"detail": "Clock-in record deleted successfully"}
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    except Exception as e:
        print(f"Error occurred while deleting clock-in record: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/clock-in/{clock_in_id}")
async def update_clock_in(clock_in_id: str, clock_in: ClockInCreate):
    try:
        clock_in_data = clock_in.dict(exclude_unset=True)
        result = await mongo_db.clock_in_collection.update_one(
            {"_id": ObjectId(clock_in_id)},
            {"$set": clock_in_data}
        )
        if result.modified_count == 1:
            return {"detail": "Clock-in record updated successfully"}
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    except Exception as e:
        print(f"Error occurred while updating clock-in record: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
