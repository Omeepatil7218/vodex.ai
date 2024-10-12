from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from app.routes import clock_in, items
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"  # Local MongoDB connection
client = AsyncIOMotorClient(MONGO_URI)
db = client['fastapi_db']  # The MongoDB database
items_collection = db['items']  # The specific collection for items

app = FastAPI()
router = APIRouter()

# Middleware to handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a route to display items
@app.get("/", response_class=HTMLResponse)
async def read_root():
    items_data = await items_collection.find().to_list(100)  # Get up to 100 items
    items_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Items List</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 20px;
                font-size: 2.5em;
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            ul {
                list-style-type: none;
                padding: 0;
                max-width: 800px;
                margin: auto;
            }
            li {
                background: #fff;
                margin: 10px 0;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s, box-shadow 0.3s;
                position: relative;
            }
            li:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            }
            .item-id {
                font-weight: bold;
                color: #007BFF;
                font-size: 1.2em;
            }
            .item-info {
                margin: 5px 0;
                color: #555;
                font-size: 1em;
            }
            .expiry-info {
                color: #FF5722;  /* Warning color */
                font-weight: bold;
            }
            /* Responsive Design */
            @media (max-width: 600px) {
                h1 {
                    font-size: 2em;
                }
                li {
                    padding: 15px;
                }
            }
        </style>
    </head>
    <body>
        <h1>Items List</h1>
        <ul>
    """
    for item in items_data:
        item_id = str(item["_id"])  # Convert ObjectId to string
        items_html += f"""
            <li>
                <span class="item-id">ID: {item_id}</span>
                <div class="item-info">Name: {item['name']}</div>
                <div class="item-info">Email: {item['email']}</div>
                <div class="item-info">Item Name: {item['item_name']}</div>
                <div class="item-info">Quantity: {item['quantity']}</div>
                <div class="item-info expiry-info">Expiry Date: {item['expiry_date']}</div>
            </li>
        """
    items_html += """
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=items_html)

# Include routers for other routes
app.include_router(items.router, prefix="/api")
app.include_router(clock_in.router, prefix="/api")
