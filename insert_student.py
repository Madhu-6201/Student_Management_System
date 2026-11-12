
from db import students_collection

# Multiple sample students
students = [
    {
        "roll_no": 301,
        "name": "Priya Sharma",
        "age": 19,
        "gender": "Female",
        "course": "BCA",
        "email": "priya@gmail.com",
        "phone": "9876543301"
    },
    {
        "roll_no": 302,
        "name": "Amit Kumar",
        "age": 22,
        "gender": "Male",
        "course": "MCA",
        "email": "amit@gmail.com",
        "phone": "9876543302"
    },
    {
        "roll_no": 303,
        "name": "Neha Singh",
        "age": 24,
        "gender": "Female",
        "course": "BTech",
        "email": "neha@gmail.com",
        "phone": "9876543303"
    },
    {
        "roll_no": 304,
        "name": "Rohit Verma",
        "age": 26,
        "gender": "Male",
        "course": "MBA",
        "email": "rohit@gmail.com",
        "phone": "9876543304"
    },
    {
        "roll_no": 305,
        "name": "Anjali Kumari",
        "age": 21,
        "gender": "Female",
        "course": "MCA",
        "email": "anjali@gmail.com",
        "phone": "9876543305"
    },
    {
        "roll_no": 306,
        "name": "Rahul Singh",
        "age": 23,
        "gender": "Male",
        "course": "BCA",
        "email": "rahul.singh@gmail.com",
        "phone": "9876543306"
    },
    {
        "roll_no": 307,
        "name": "Pooja Gupta",
        "age": 20,
        "gender": "Female",
        "course": "BTech",
        "email": "pooja@gmail.com",
        "phone": "9876543307"
    },
    {
        "roll_no": 308,
        "name": "Vikash Kumar",
        "age": 25,
        "gender": "Male",
        "course": "MBA",
        "email": "vikash@gmail.com",
        "phone": "9876543308"
    },
    {
        "roll_no": 309,
        "name": "Sneha Verma",
        "age": 22,
        "gender": "Female",
        "course": "MCA",
        "email": "sneha@gmail.com",
        "phone": "9876543309"
    },
    {
        "roll_no": 310,
        "name": "Arjun Sharma",
        "age": 27,
        "gender": "Male",
        "course": "BCA",
        "email": "arjun@gmail.com",
        "phone": "9876543310"
    },
    {
        "roll_no": 311,
        "name": "Riya Kumari",
        "age": 19,
        "gender": "Female",
        "course": "MBA",
        "email": "riya@gmail.com",
        "phone": "9876543311"
    },
    {
        "roll_no": 312,
        "name": "Deepak Singh",
        "age": 24,
        "gender": "Male",
        "course": "BTech",
        "email": "deepak@gmail.com",
        "phone": "9876543312"
    },
    {
        "roll_no": 313,
        "name": "Kajal Sharma",
        "age": 21,
        "gender": "Female",
        "course": "MCA",
        "email": "kajal@gmail.com",
        "phone": "9876543313"
    },
    {
        "roll_no": 314,
        "name": "Manish Gupta",
        "age": 26,
        "gender": "Male",
        "course": "BCA",
        "email": "manish@gmail.com",
        "phone": "9876543314"
    },
    {
        "roll_no": 315,
        "name": "Simran Kaur",
        "age": 23,
        "gender": "Female",
        "course": "BTech",
        "email": "simran@gmail.com",
        "phone": "9876543315"
    },
    {
        "roll_no": 316,
        "name": "Aditya Verma",
        "age": 28,
        "gender": "Male",
        "course": "MBA",
        "email": "aditya@gmail.com",
        "phone": "9876543316"
    },
    {
        "roll_no": 317,
        "name": "Nisha Kumari",
        "age": 20,
        "gender": "Female",
        "course": "MCA",
        "email": "nisha@gmail.com",
        "phone": "9876543317"
    },
    {
        "roll_no": 318,
        "name": "Mohit Kumar",
        "age": 25,
        "gender": "Male",
        "course": "BCA",
        "email": "mohit@gmail.com",
        "phone": "9876543318"
    },
    {
        "roll_no": 319,
        "name": "Divya Singh",
        "age": 22,
        "gender": "Female",
        "course": "BTech",
        "email": "divya@gmail.com",
        "phone": "9876543319"
    },
    {
        "roll_no": 320,
        "name": "Gaurav Sharma",
        "age": 24,
        "gender": "Male",
        "course": "MBA",
        "email": "gaurav@gmail.com",
        "phone": "9876543320"
    },
    {
        "roll_no": 321,
        "name": "Ananya Gupta",
        "age": 19,
        "gender": "Female",
        "course": "MCA",
        "email": "ananya@gmail.com",
        "phone": "9876543321"
    },
    {
        "roll_no": 322,
        "name": "Ravi Kumar",
        "age": 27,
        "gender": "Male",
        "course": "BCA",
        "email": "ravi@gmail.com",
        "phone": "9876543322"
    },
    {
        "roll_no": 323,
        "name": "Komal Verma",
        "age": 21,
        "gender": "Female",
        "course": "BTech",
        "email": "komal@gmail.com",
        "phone": "9876543323"
    },
    {
        "roll_no": 324,
        "name": "Abhishek Singh",
        "age": 26,
        "gender": "Male",
        "course": "MBA",
        "email": "abhishek@gmail.com",
        "phone": "9876543324"
    },
    {
        "roll_no": 325,
        "name": "Shivani Gupta",
        "age": 23,
        "gender": "Female",
        "course": "MCA",
        "email": "shivani@gmail.com",
        "phone": "9876543325"
    },
    {
        "roll_no": 326,
        "name": "Nitin Kumar",
        "age": 20,
        "gender": "Male",
        "course": "BCA",
        "email": "nitin@gmail.com",
        "phone": "9876543326"
    },
    {
        "roll_no": 327,
        "name": "Sakshi Sharma",
        "age": 25,
        "gender": "Female",
        "course": "BTech",
        "email": "sakshi@gmail.com",
        "phone": "9876543327"
    },
    {
        "roll_no": 328,
        "name": "Harsh Verma",
        "age": 28,
        "gender": "Male",
        "course": "MBA",
        "email": "harsh@gmail.com",
        "phone": "9876543328"
    },
    {
        "roll_no": 329,
        "name": "Payal Kumari",
        "age": 22,
        "gender": "Female",
        "course": "MCA",
        "email": "payal@gmail.com",
        "phone": "9876543329"
    },
    {
        "roll_no": 330,
        "name": "Varun Singh",
        "age": 24,
        "gender": "Male",
        "course": "BCA",
        "email": "varun@gmail.com",
        "phone": "9876543330"
    },
    {
        "roll_no": 331,
        "name": "Isha Gupta",
        "age": 19,
        "gender": "Female",
        "course": "BTech",
        "email": "isha@gmail.com",
        "phone": "9876543331"
    },
    {
        "roll_no": 332,
        "name": "Pankaj Sharma",
        "age": 27,
        "gender": "Male",
        "course": "MBA",
        "email": "pankaj@gmail.com",
        "phone": "9876543332"
    },
    {
        "roll_no": 333,
        "name": "Aarti Singh",
        "age": 21,
        "gender": "Female",
        "course": "MCA",
        "email": "aarti@gmail.com",
        "phone": "9876543333"
    },
    {
        "roll_no": 334,
        "name": "Sahil Kumar",
        "age": 26,
        "gender": "Male",
        "course": "BCA",
        "email": "sahil@gmail.com",
        "phone": "9876543334"
    },
    {
        "roll_no": 335,
        "name": "Ritika Verma",
        "age": 23,
        "gender": "Female",
        "course": "BTech",
        "email": "ritika@gmail.com",
        "phone": "9876543335"
    },
    {
        "roll_no": 336,
        "name": "Ajay Gupta",
        "age": 25,
        "gender": "Male",
        "course": "MBA",
        "email": "ajay@gmail.com",
        "phone": "9876543336"
    },
    {
        "roll_no": 337,
        "name": "Kavita Kumari",
        "age": 20,
        "gender": "Female",
        "course": "MCA",
        "email": "kavita@gmail.com",
        "phone": "9876543337"
    },
    {
        "roll_no": 338,
        "name": "Yash Sharma",
        "age": 28,
        "gender": "Male",
        "course": "BCA",
        "email": "yash@gmail.com",
        "phone": "9876543338"
    },
    {
        "roll_no": 339,
        "name": "Swati Singh",
        "age": 22,
        "gender": "Female",
        "course": "BTech",
        "email": "swati@gmail.com",
        "phone": "9876543339"
    },
    {
        "roll_no": 340,
        "name": "Rakesh Verma",
        "age": 24,
        "gender": "Male",
        "course": "MBA",
        "email": "rakesh@gmail.com",
        "phone": "9876543340"
    },
    {
        "roll_no": 341,
        "name": "Muskan Gupta",
        "age": 19,
        "gender": "Female",
        "course": "MCA",
        "email": "muskan@gmail.com",
        "phone": "9876543341"
    },
    {
        "roll_no": 342,
        "name": "Tarun Kumar",
        "age": 27,
        "gender": "Male",
        "course": "BCA",
        "email": "tarun@gmail.com",
        "phone": "9876543342"
    },
    {
        "roll_no": 343,
        "name": "Preeti Sharma",
        "age": 21,
        "gender": "Female",
        "course": "BTech",
        "email": "preeti@gmail.com",
        "phone": "9876543343"
    },
    {
        "roll_no": 344,
        "name": "Abhay Singh",
        "age": 26,
        "gender": "Male",
        "course": "MBA",
        "email": "abhay@gmail.com",
        "phone": "9876543344"
    },
    {
        "roll_no": 345,
        "name": "Monika Kumari",
        "age": 23,
        "gender": "Female",
        "course": "MCA",
        "email": "monika@gmail.com",
        "phone": "9876543345"
    },
    {
        "roll_no": 346,
        "name": "Aman Verma",
        "age": 20,
        "gender": "Male",
        "course": "BCA",
        "email": "aman@gmail.com",
        "phone": "9876543346"
    },
    {
        "roll_no": 347,
        "name": "Tanya Gupta",
        "age": 25,
        "gender": "Female",
        "course": "BTech",
        "email": "tanya@gmail.com",
        "phone": "9876543347"
    },
    {
        "roll_no": 348,
        "name": "Gopal Kumar",
        "age": 28,
        "gender": "Male",
        "course": "MBA",
        "email": "gopal@gmail.com",
        "phone": "9876543348"
    },
    {
        "roll_no": 349,
        "name": "Meena Singh",
        "age": 22,
        "gender": "Female",
        "course": "MCA",
        "email": "meena@gmail.com",
        "phone": "9876543349"
    },
    {
        "roll_no": 350,
        "name": "Vivek Sharma",
        "age": 24,
        "gender": "Male",
        "course": "BCA",
        "email": "vivek@gmail.com",
        "phone": "9876543350"
    }
]

# Remove only previous sample records in this roll number range.
# This prevents duplicate roll number errors when rerunning this script.
students_collection.delete_many({
    "roll_no": {"$gte": 301, "$lte": 350}
})

# Insert multiple students into MongoDB
result = students_collection.insert_many(students)

print("Students Added Successfully!")
print("Total Students Inserted:", len(result.inserted_ids))
print("Inserted Student IDs:")

for student_id in result.inserted_ids:
    print(student_id)

print("Total Students in Database:",
      students_collection.count_documents({}))
