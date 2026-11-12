from db import courses_collection

# Courses Data
courses = [
    {
        "course_code": "MCA",
        "course_name": "Master of Computer Applications",
        "duration": "2 Years",
        "department": "Computer Science"
    },
    {
        "course_code": "BCA",
        "course_name": "Bachelor of Computer Applications",
        "duration": "3 Years",
        "department": "Computer Science"
    },
    {
        "course_code": "BTech",
        "course_name": "Bachelor of Technology",
        "duration": "4 Years",
        "department": "Engineering"
    },
    {
        "course_code": "MBA",
        "course_name": "Master of Business Administration",
        "duration": "2 Years",
        "department": "Management"
    }
]

# Insert or Update Courses
for course in courses:
    courses_collection.update_one(
        {"course_code": course["course_code"]},
        {"$set": course},
        upsert=True
    )

print("Courses Added Successfully!")
print("Total Courses:", courses_collection.count_documents({}))