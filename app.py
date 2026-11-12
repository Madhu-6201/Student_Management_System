
import re
from flask import Flask, render_template, request, redirect, url_for, flash
from db import students_collection, courses_collection

app = Flask(__name__)
app.secret_key = "student_management_secret_key"


# Dashboard
@app.route("/")
def home():

    total_students = students_collection.count_documents({})
    total_courses = len(students_collection.distinct("course"))

    return render_template(
        "index.html",
        total_students=total_students,
        total_courses=total_courses
    )


# Add Student Page
@app.route("/add_student")
def add_student_page():
    return render_template("add_student.html")
    
    
# View Students with Search and Course Filter
@app.route("/view_students")
def view_students():

    search_query = request.args.get("search", "").strip()
    selected_course = request.args.get("course", "")

    query_filter = {}

    # Search by Name or Roll Number
    if search_query:
        search_conditions = [
            {
                "name": {
                    "$regex": re.escape(search_query),
                    "$options": "i"
                }
            }
        ]

        if search_query.isdigit():
            search_conditions.append(
                {"roll_no": int(search_query)}
            )

        query_filter["$or"] = search_conditions

    # Filter by Course
    if selected_course in ["MCA", "BCA", "BTech", "MBA"]:
        query_filter["course"] = selected_course

    # Fetch Students from MongoDB
    all_students = list(
        students_collection.find(query_filter).sort("roll_no", 1)
    )

    return render_template(
        "view_students.html",
        students=all_students,
        search_query=search_query,
        selected_course=selected_course
    )



# Save Student in MongoDB with Validation
@app.route("/add_student", methods=["POST"])
def add_student():

    try:
        roll_no = int(request.form.get("roll_no", ""))
        age = int(request.form.get("age", ""))

        name = request.form.get("name", "").strip()
        gender = request.form.get("gender", "")
        course = request.form.get("course", "")
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()

        # Roll Number Validation
        if roll_no <= 0:
            flash("Roll number must be greater than 0.", "error")
            return redirect(url_for("add_student_page"))

        # Age Validation
        if age < 1 or age > 100:
            flash("Please enter a valid age between 1 and 100.", "error")
            return redirect(url_for("add_student_page"))

        # Name Validation
        if len(name) < 2 or len(name) > 50 or not name.replace(" ", "").isalpha():
            flash("Please enter a valid student name.", "error")
            return redirect(url_for("add_student_page"))

        # Gender Validation
        if gender not in ["Male", "Female", "Other"]:
            flash("Please select a valid gender.", "error")
            return redirect(url_for("add_student_page"))

        # Course Validation
        if course not in ["MCA", "BCA", "BTech", "MBA"]:
            flash("Please select a valid course.", "error")
            return redirect(url_for("add_student_page"))

        # Email Validation
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("add_student_page"))

        # Phone Validation
        if not re.fullmatch(r"[0-9]{10}", phone):
            flash("Phone number must contain exactly 10 digits.", "error")
            return redirect(url_for("add_student_page"))

        # Duplicate Roll Number Check
        existing_student = students_collection.find_one(
            {"roll_no": roll_no}
        )

        if existing_student:
            flash("Roll number already exists!", "error")
            return redirect(url_for("add_student_page"))

        # Save Student
        student = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "gender": gender,
            "course": course,
            "email": email,
            "phone": phone
        }

        students_collection.insert_one(student)

        flash("Student added successfully!", "success")
        return redirect(url_for("view_students"))

    except ValueError:
        flash("Please enter valid numeric values.", "error")
        return redirect(url_for("add_student_page"))


# Edit Student with Backend Validation
@app.route("/edit_student/<int:roll_no>", methods=["GET", "POST"])
def edit_student(roll_no):

    student = students_collection.find_one({"roll_no": roll_no})

    if student is None:
        flash("Student not found!", "error")
        return redirect(url_for("view_students"))

    if request.method == "POST":

        try:
            name = request.form.get("name", "").strip()
            age = int(request.form.get("age", ""))

            gender = request.form.get("gender", "")
            course = request.form.get("course", "")
            email = request.form.get("email", "").strip()
            phone = request.form.get("phone", "").strip()

            # Name Validation
            if len(name) < 2 or len(name) > 50 or not name.replace(" ", "").isalpha():
                flash("Please enter a valid student name.", "error")
                return redirect(url_for("edit_student", roll_no=roll_no))

            # Age Validation
            if age < 1 or age > 100:
                flash("Age must be between 1 and 100.", "error")
                return redirect(url_for("edit_student", roll_no=roll_no))

            # Gender Validation
            if gender not in ["Male", "Female", "Other"]:
                flash("Please select a valid gender.", "error")
                return redirect(url_for("edit_student", roll_no=roll_no))

            # Course Validation
            if course not in ["MCA", "BCA", "BTech", "MBA"]:
                flash("Please select a valid course.", "error")
                return redirect(url_for("edit_student", roll_no=roll_no))

            # Email Validation
            if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
                flash("Please enter a valid email address.", "error")
                return redirect(url_for("edit_student", roll_no=roll_no))

            # Phone Validation
            if not re.fullmatch(r"[0-9]{10}", phone):
                flash("Phone number must contain exactly 10 digits.", "error")
                return redirect(url_for("edit_student", roll_no=roll_no))

            # Update Student in MongoDB
            updated_student = {
                "name": name,
                "age": age,
                "gender": gender,
                "course": course,
                "email": email,
                "phone": phone
            }

            students_collection.update_one(
                {"roll_no": roll_no},
                {"$set": updated_student}
            )

            flash("Student updated successfully!", "success")
            return redirect(url_for("view_students"))

        except ValueError:
            flash("Please enter a valid age.", "error")
            return redirect(url_for("edit_student", roll_no=roll_no))

    return render_template(
        "edit_student.html",
        student=student
    )


# Delete Student
@app.route("/delete_student/<int:roll_no>", methods=["POST"])
def delete_student(roll_no):

    result = students_collection.delete_one(
        {"roll_no": roll_no}
    )

    if result.deleted_count > 0:
        flash("Student deleted successfully!", "success")
    else:
        flash("Student not found!", "error")

    return redirect(url_for("view_students"))

# MongoDB Operations Dashboard

@app.route("/database_dashboard")
def database_dashboard():

    total_students = students_collection.count_documents({})
    total_courses = courses_collection.count_documents({})

    student_indexes = list(students_collection.list_indexes())
    course_indexes = list(courses_collection.list_indexes())

    database_name = students_collection.database.name

    return render_template(
        "database_dashboard.html",
        total_students=total_students,
        total_courses=total_courses,
        student_indexes=student_indexes,
        course_indexes=course_indexes,
        database_name=database_name
    )

# Run Flask Application
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
