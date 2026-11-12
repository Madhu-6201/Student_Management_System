
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database reference
db = client["StudentDB"]

# Create collection reference
students_collection = db["students"]
courses_collection = db["courses"]

# Check connection
try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")
    print("Database: StudentDB")
    print("Collection: students")
    print("Collection: courses")

except Exception as e:
    print("Connection Error:", e)
