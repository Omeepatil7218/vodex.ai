FastAPI CRUD Application with MongoDB

This project is a FastAPI-based application that performs CRUD (Create, Read, Update, Delete) operations on Items and manages Clock-In Records.
The data is stored in a MongoDB database,and the application is deployed on a free hosting platform with API documentation available via Swagger UI.

Features::
FastAPI for building APIs efficiently.
MongoDB for storing items and clock-in records.
CRUD operations for managing items.
MongoDB Aggregation for filtering and querying.
CORS middleware to allow cross-origin requests.
Swagger UI for automatic API documentation.


Here’s a well-structured README.md file for your FastAPI project that covers setup, explanation of endpoints, and other necessary details:

FastAPI CRUD Application with MongoDB
This project is a FastAPI-based application that performs CRUD (Create, Read, Update, Delete) operations on Items and manages Clock-In Records. The data is stored in a MongoDB database, and the application is deployed on a free hosting platform with API documentation available via Swagger UI.

Features
FastAPI for building APIs efficiently.
MongoDB for storing items and clock-in records.
CRUD operations for managing items.
MongoDB Aggregation for filtering and querying.
CORS middleware to allow cross-origin requests.
Swagger UI for automatic API documentation.

Table of Contents::
Project Setup
Environment Variables
Running the Application Locally
API Endpoints
Deployment
Contributing

Project Setup::
Clone the repository:

bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Create a virtual environment::
python -m venv myenv
source myenv/bin/activate 

  
Install the dependencies:

pip install -r requirements.txt
Set up MongoDB:::
Install MongoDB locally or use a cloud solution like MongoDB Atlas.
Update the MongoDB connection URI in the .env file.
Environment Variables::;
Create a .env file in the root directory and add the following:
MONGO_URI=mongodb://localhost:27017/fastapi_db  # Adjust based on your MongoDB setup
SECRET_KEY=your-secret-key
Running the Application Locally
Start MongoDB: Make sure MongoDB is running locally or is accessible via a cloud service.

Run the FastAPI application:::
uvicorn app.main:app --reload

Access the application:::
Open http://127.0.0.1:8000 to view the homepage.
Access the Swagger UI at http://127.0.0.1:8000/docs for API documentation and interactive testing.


API Endpoints::
1. Items API
Method	Endpoint	Description
POST	/api/items/	Create a new item
GET	/api/items/{id}	Retrieve an item by ID
PUT	/api/items/{id}	Update an item by ID
DELETE	/api/items/{id}	Delete an item by ID
GET	/	Display all items (HTML)

3. Clock-In Records API::
Method	Endpoint	Description
POST	/api/clock_in/	Create a new clock-in record
GET	/api/clock_in/{id}	Retrieve a clock-in record by ID


Sample Payload for Items::
json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "item_name": "Laptop",
  "quantity": 5,
  "expiry_date": "2025-10-12T05:20:29.615Z"
}

Contributing
If you’d like to contribute to the project, feel free to open an issue or submit a pull request.
