# Import necessary modules
import os
import requests
from flask import jsonify
from flask import Flask, request, redirect, url_for, render_template, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import flash_message, login_required, generate_secret_key, validate_class_name, check_required_fields, get_new_study_materials

# Create a Flask web application instance
app = Flask(__name__)

# Configure session settings
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = generate_secret_key(64)
Session(app)

# Connect to the SQLite database
db = SQL("sqlite:///learntogether.db")

# Define route for the homepage, accessible only to logged-in users
@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    # Retrieve assignments for the logged-in student
    assignment = db.execute("SELECT * FROM assignment WHERE student_id = ?", session["user_id"])
    # Render the homepage template with assignment data
    return render_template("index.html", assignment=assignment)

# Define route for user signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Clear any existing session data
    session.clear()
    
    # Handle POST request for user signup
    if request.method == "POST":
        # Extract user input from the form
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        class_name = request.form.get("class")
        
        # Check if all required fields are provided
        result = check_required_fields({"Full Name": full_name, "Email": email, "Password": password, "Class Name": class_name}, current_page="signup")
        if result:
            return result
        
        # Validate the format of the class name
        if not validate_class_name(class_name):
            flash_message("Class Name must adhere to the specified convention. i.e(CS50, CS or any acronym)", category='info')
            return render_template("signup.html")
        
        # Check if the provided email already exists in the database
        email_exists = db.execute("SELECT * FROM students WHERE email = ?", email)
        if email_exists:
            flash_message("Email is already exist. Please Login Instead.", category='info')
            return render_template("signup.html")

        # Hash the password before storing it in the database
        hash_password = generate_password_hash(password)
        
        # Insert user data into the database
        db.execute("INSERT INTO students (full_name, email, password, class_name, role) VALUES (?, ?, ?, ?, ?)", full_name, email, hash_password, class_name, 'student')
        
        # Display a success message and redirect to the login page
        flash_message("Signup successful!", category='success')
        return render_template("login.html")
    
    # Render the signup page for GET requests
    return render_template("signup.html")

# Define route for user login
@app.route("/login", methods=["GET", "POST"])
def login():
    # Clear any existing session data
    session.clear()
    
    # Display a logout message if the request includes a logout parameter
    if request.args.get('logout'):
        flash_message("You're Logout!", category='success')
    
    # Handle POST request for user login
    if request.method == "POST":
        # Extract user input from the form
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check if email and password are provided
        if not email or not password:
            flash_message("Provide required Fields to Log In!", category='error')
            return render_template("login.html")
        
        # Retrieve user data from the database based on the provided email
        student = db.execute("SELECT * FROM students WHERE email = ?", email)
        
        # Check if the user exists and the password is correct
        if not student or not check_password_hash(student[0]["password"], password):
            flash_message("Invalid email or password!", category='error')
            return render_template("login.html")
        
        # Store the user ID in the session for authentication
        session["user_id"] = student[0]["id"]
        # Display a success message and redirect to the homepage
        flash_message("Log In Successful!", category='success')
        return redirect(url_for("index"))
    
    # Render the login page for GET requests
    return render_template("login.html")

# Define route for user logout
@app.route("/logout")
@login_required
def logout():
    # Clear the session data
    session.clear()
    # Redirect to the login page with a logout parameter
    return redirect(url_for('login', logout=True))

# Define route for displaying classes
@app.route("/classes")
@login_required
def classes():
    # Render the classes template
    return render_template("classes.html")

# Define route for creating assignments
@app.route("/assign", methods=['GET', 'POST'])
@login_required
def assign():
    # Handle POST request for creating assignments
    if request.method == 'POST':
        name = request.form.get('assignment_name')
        subject = request.form.get('subject')
        description = request.form.get('assignment_description')
        
        # Check if assignment details are provided
        if name and subject and description:
            # Insert assignment data into the database
            db.execute("INSERT INTO assignment (student_id, name, subject, description) VALUES (?, ?, ?, ?)", session["user_id"], name, subject, description)
    
    # Redirect to the homepage
    return redirect("/")

# Define route for displaying exams
@app.route("/exams")
@login_required
def exams():
    # Render the exams template
    return render_template("exams.html")

# Define route for displaying messages
@app.route("/messages")
@login_required
def messages():
    # Render the messages template
    return render_template("messages.html")

# Define route for submitting complaints or requests
@app.route("/complaint", methods=["GET", "POST"])
@login_required
def complaint():
    # Handle POST request for submitting complaints or requests
    if request.method == "POST":
        submission_type = request.form.get("submissionType")
        category = request.form.get("category")
        subject = request.form.get("subject")
        description = request.form.get("description")
    
        # Check if all required fields are provided
        result = check_required_fields({"Submission Type": submission_type, "Category": category, "Subject": subject, "Description": description}, current_page="complaint_or_request")
        if result:
            return result
        
        # Insert complaint or request data into the database
        db.execute("INSERT INTO complaints_requests (student_id, submission_type, category, subject, description) VALUES (?, ?, ?, ?, ?)", session["user_id"], submission_type, category, subject, description)
        
        # Display a success message and redirect to the homepage
        flash_message("Your Complaint or request submitted successfully!", category="success")
        return redirect(url_for("index"))
    
    # Render the complaints or requests form for GET requests
    return render_template("complaint_or_request.html")


# Route to render the study materials page
@app.route('/study_materials', methods=['GET'])
def study_materials():
    study_new_materials_data = get_new_study_materials(db, session)
    return jsonify(study_new_materials_data)


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
