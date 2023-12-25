import os

import  requests
from flask import Flask, request, redirect, url_for, render_template, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import flash_message, login_required, generate_secret_key, validate_class_name, check_required_fields

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = generate_secret_key(64)
Session(app)

# Sever static files
app.config["STATIC_FOLDER"] = "static"

# SQL Database for sudents
db = SQL("sqlite:///learntogether.db")

# Routes
@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    # if request.method == "POST":
    #     try:
    #         job_query = request.form['job']

    #         # Perform the API request with the job query
    #         api_url = "https://jsearch.p.rapidapi.com/search"
    #         api_headers = {
    #             'X-RapidAPI-Key': '648d1a0acamsheeb1c88c3ed9679p1b37ecjsn2133e3d076b0',
    #             'X-RapidAPI-Host': 'jsearch.p.rapidapi.com'
    #         }
    #         api_params = {
    #             'query': job_query,
    #             'page': '1',
    #             'num_pages': '1'
    #         }

    #         response = requests.get(api_url, headers=api_headers, params=api_params)
    #         jobs_data = response
            
    #         flash_message("Jobs are founded", category="success")
    #         return render_template("index.html", jobs_data=jobs_data)
            
    #     except Exception as e:
    #         e = f"Error: {e}"
    #         flash_message(e, category="error")
    #         return render_template("index.html")
    
    # name = db.execute("SELECT full_name FROM students WHERE id = ?", session["user_id"])
    assignment = db.execute("SELECT * FROM assignment WHERE student_id = ?", session["user_id"])
    return render_template("index.html", assignment=assignment)
    

@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Initialize the session
    session.clear()
    
    # For user request post
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        class_name = request.form.get("class")
        
        # Using the helper function to check requried fields
        result = check_required_fields({"Full Name": full_name, "Email": email, "Password": password, "Class Name": class_name}, current_page="signup")
        
        # If True, return, otherwise, move forward
        if result:
            return result
        
        # Validate Class Name using the helper Function
        if not validate_class_name(class_name):
            flash_message("Class Name must adhere to the specified convention. i.e(CS50, CS or any acronym)", category='info')
            # return redirect(url_for('show_flash'))
            return render_template("signup.html")
        
        # Check if the email already exits
        email_exits = db.execute("SELECT * FROM students WHERE email = ?", email)
        if email_exits:
            flash_message("Email is already exist. Please Login Instead.", category='info')
            # return redirect(url_for('show_flash'))
            return render_template("singup.html")

        # Secure the password
        hash_password = generate_password_hash(password)
        
        # INSERT DATA INTO DATABASE
        db.execute("INSERT INTO students (full_name, email, password, class_name, role) VALUES (?, ?, ?, ?, ?)", full_name, email, hash_password, class_name, 'student')
        
        # Show Sign Up successful message to user
        flash_message("Signup successful!", category='success')
        # return render_template("singup.html")
        
        # Retrieve the newly inserted student's data
        # student = db.execute("SELECT * FROM students WHERE email = ?", email)
        
        # Redirect user to login page
        # return redirect(url_for("login"))
        return render_template("login.html")
    
    # if user request is get
    return render_template("signup.html")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    # Clear session data
    session.clear()
    
    if request.args.get('logout'):
        flash_message("You're Logout!", category='success')
    
    # If request method is POST then
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check the user input 
        if not email or not password:
            flash_message("Provide required Fields to Log In!", category='error')
            # return redirect(url_for('show_flash'))
            return render_template("login.html")
        
        # Check if the email already exits
        student = db.execute("SELECT * FROM students WHERE email = ?", email)
        
        # Validate the user email and password
        if not student or not check_password_hash(student[0]["password"], password):
            flash_message("Invalid email or password!", category='error')
            # return redirect(url_for('show_flash'))
            return render_template("login.html")
        
        # Store user id in session
        session["user_id"] = student[0]["id"]
        
        # Redirect to the index.html after successful login
        flash_message("Log In Successful!", category='success')
        return redirect(url_for("index"))
    
    # Request method is GET
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for('login', logout=True))


@app.route("/classes")
@login_required
def classes():
    return render_template("classes.html")


@app.route("/assign", methods=['GET', 'POST'])
@login_required
def assign():
    if request.method == 'POST':
        name = request.form.get('assignment_name')
        subject = request.form.get('subject')
        description = request.form.get('assignment_description')
        
        if name and subject and description:
            db.execute("INSERT INTO assignment (student_id, name, subject, description) VALUES (?, ?, ?, ?)", session["user_id"], name, subject, description)
    
    return redirect("/")


@app.route("/exams")
@login_required
def exams():
    return render_template("exams.html")


@app.route("/messages")
@login_required
def messages():
    return render_template("messages.html")


# Route user for sumbmitting complaints or requests
@app.route("/complaint", methods=["GET", "POST"] )
@login_required
def complaint():
    if request.method == "POST":
        # Retrieve user given data
        submission_type = request.form.get("submissionType")
        category = request.form.get("category")
        subject = request.form.get("subject")
        description = request.form.get("description")
    
        # Validate required fields
        result = check_required_fields({
            "Submission Type": submission_type,
            "Category": category,
            "Subject": subject,
            "Description": description
        }, current_page="complaint_or_request")
        
        # If true, return, otherwise, move forward
        if result:
            return result
        
        # Now it's time to Insert complaint or request into the database
        db.execute("INSERT INTO complaints_requests (student_id, submission_type, category, subject, description) VALUES (?, ?, ?, ?, ?)", session["user_id"], submission_type, category, subject, description)
        
        # Show success message to the user
        flash_message("Your Complaint or request submitted successfully!", category="success")

        # Redirect user to the index or any other appropriate page
        return redirect(url_for("index"))
    
    return render_template("complaint_or_request.html")


@app.route("/search")
def search():
    return render_template('show_flash.html')


if __name__ == '__main__':
    app.run(debug=True)