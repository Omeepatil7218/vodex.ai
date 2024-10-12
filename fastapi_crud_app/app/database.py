from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"  # Local MongoDB connection

class MongoDB:
    def __init__(self, uri: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client['fastapi_db']  # Database name
        self.clock_in_collection = self.db['clock_in']  # Collection for clock-ins
        self.items_collection = self.db['items']  # Collection for items

    async def connect(self):
        # Connect to MongoDB
        pass  # Connection is established when client is created

    async def close(self):
        """Close the MongoDB connection."""
        await self.client.close()

# Create an instance of MongoDB
mongo_db = MongoDB(MONGO_URI)
