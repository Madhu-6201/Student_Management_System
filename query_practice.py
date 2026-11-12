
from db import students_collection

# 1. $gt - Greater Than
print("\n1. Students whose age is greater than 20:")

students = students_collection.find({
    "age": {"$gt": 20}
})

for student in students:
    print(student["name"], "-", student["age"])


# 2. $lt - Less Than
print("\n2. Students whose age is less than 25:")

students = students_collection.find({
    "age": {"$lt": 25}
})

for student in students:
    print(student["name"], "-", student["age"])


# 3. $gte - Greater Than or Equal
print("\n3. Students whose age is greater than or equal to 22:")

students = students_collection.find({
    "age": {"$gte": 22}
})

for student in students:
    print(student["name"], "-", student["age"])


# 4. $lte - Less Than or Equal
print("\n4. Students whose age is less than or equal to 22:")

students = students_collection.find({
    "age": {"$lte": 22}
})

for student in students:
    print(student["name"], "-", student["age"])


# 5. $in - Match Any Value
print("\n5. Students enrolled in MCA or BCA:")

students = students_collection.find({
    "course": {"$in": ["MCA", "BCA"]}
})

for student in students:
    print(student["name"], "-", student["course"])
    
    
    
# MongoDB Aggregation Pipeline

print("\nCourse-wise Student Count:")

pipeline = [
    {
        "$group": {
            "_id": "$course",
            "total_students": {"$sum": 1}
        }
    }
]

result = students_collection.aggregate(pipeline)

for course in result:
    print(course)
    
    
# Course-wise Average Age

print("\nCourse-wise Average Age:")

pipeline = [
    {
        "$group": {
            "_id": "$course",
            "average_age": {"$avg": "$age"}
        }
    }
]

result = students_collection.aggregate(pipeline)

for course in result:
    print(course)
    
# $match + $group Aggregation

print("\nCourse-wise Student Count (Age > 21):")

pipeline = [
    {
        "$match": {
            "age": {"$gt": 21}
        }
    },
    {
        "$group": {
            "_id": "$course",
            "total_students": {"$sum": 1}
        }
    }
]

result = students_collection.aggregate(pipeline)

for course in result:
    print(course)
    
# $group + $sort + $project

print("\nCourse-wise Student Count (Sorted):")

pipeline = [
    {
        "$group": {
            "_id": "$course",
            "total_students": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "total_students": -1
        }
    },
    {
        "$project": {
            "_id": 0,
            "course_name": "$_id",
            "total_students": 1
        }
    }
]

result = students_collection.aggregate(pipeline)

for course in result:
    print(course)
    
# $count Aggregation

print("\nTotal Students with Age Greater Than 21:")

pipeline = [
    {
        "$match": {
            "age": {"$gt": 21}
        }
    },
    {
        "$count": "total_students"
    }
]

result = students_collection.aggregate(pipeline)

for data in result:
    print(data)
    
    



from db import students_collection

# MongoDB $lookup

print("\nStudents with Course Details:")

pipeline = [
    {
        "$lookup": {
            "from": "courses",
            "localField": "course",
            "foreignField": "course_code",
            "as": "course_details"
        }
    }
]

result = students_collection.aggregate(pipeline)

for student in result:
    print("Student Name:", student["name"])
    print("Course:", student["course"])
    print("Course Details:", student["course_details"])
    print("--------------------------------")
    
# $lookup + $unwind

print("\nStudent Details with Course Information:")

pipeline = [
    {
        "$lookup": {
            "from": "courses",
            "localField": "course",
            "foreignField": "course_code",
            "as": "course_details"
        }
    },
    {
        "$unwind": "$course_details"
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "course": 1,
            "course_details.course_name": 1,
            "course_details.duration": 1,
            "course_details.department": 1
        }
    }
]

result = students_collection.aggregate(pipeline)

for student in result:
    print(student)
    
# MongoDB Indexing

print("\nCreating Index on Roll Number:")

index_name = students_collection.create_index("roll_no")

print("Index Created Successfully!")
print("Index Name:", index_name)

print("\nAvailable Indexes:")

for index in students_collection.list_indexes():
    print(index)
    
# Search Student Using Indexed Roll Number

print("\nSearching Student Using Roll Number:")

student = students_collection.find_one({"roll_no": 325})

if student:
    print("Student Found!")
    print("Name:", student["name"])
    print("Roll Number:", student["roll_no"])
    print("Course:", student["course"])
else:
    print("Student Not Found!")

