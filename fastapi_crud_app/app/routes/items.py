from fastapi import APIRouter, HTTPException
from app.schemas import ItemCreate, ItemUpdate
from app.database import mongo_db
import datetime
from bson import ObjectId

router = APIRouter()

@router.post("/items")
async def create_item(item: ItemCreate):
    try:
        item_data = item.dict()
        item_data["insert_date"] = datetime.datetime.now()
        result = await mongo_db.items_collection.insert_one(item_data)
        item_data["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return item_data
    except Exception as e:
        print(f"Error occurred while creating item: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/items/{item_id}")
async def get_item(item_id: str):
    try:
        item = await mongo_db.items_collection.find_one({"_id": ObjectId(item_id)})
        if item:
            item["_id"] = str(item["_id"])  # Convert ObjectId to string
            return item
        raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        print(f"Error occurred while retrieving item: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    try:
        result = await mongo_db.items_collection.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count == 1:
            return {"detail": "Item deleted successfully"}
        raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        print(f"Error occurred while deleting item: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/items/{item_id}")
async def update_item(item_id: str, item: ItemUpdate):
    try:
        item_data = item.dict(exclude_unset=True)  # Exclude unset fields
        result = await mongo_db.items_collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": item_data}
        )
        if result.modified_count == 1:
            return {"detail": "Item updated successfully"}
        raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        print(f"Error occurred while updating item: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
