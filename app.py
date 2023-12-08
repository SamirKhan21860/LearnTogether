import os

import secrets
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import flash_message, login_required, generate_secret_key, validate_class_name, check_required_fields

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = generate_secret_key(64)
Session(app)

# SQL Database for sudents
db = SQL("sqlite:///learntogether.db")

# Routes
@app.route("/")
@login_required
def index():
    name = db.execute("SELECT full_name FROM students WHERE id = ?", session["user_id"])
    return render_template("index.html", student=name)
    

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
        result = check_required_fields({"Full Name": full_name, "Email": email, "Password": password, "Class Name": class_name})
        
        # If True, return, otherwise, move forward
        if result:
            return result
        
        # Validate Class Name using the helper Function
        if not validate_class_name(class_name):
            flash_message("Class Name must adhere to the specified convention.")
            return redirect(url_for('show_flash'))
        
        # Check if the email already exits
        email_exits = db.execute("SELECT * FROM students WHERE email = ?", email)
        if email_exits:
            flash_message("Email is already exist. Please Login Instead.", category='info')
            # return redirect(url_for('show_flash'))
            return

        # Secure the password
        hash_password = generate_password_hash(password)
        
        # INSERT DATA INTO DATABASE
        db.execute("INSERT INTO students (full_name, email, password, class_name, role) VALUES (?, ?, ?, ?, ?)", full_name, email, hash_password, class_name, 'student')
        
        # Show Sign Up successful message to user
        flash_message("Signup successful!", category='success')
        
        # Retrieve the newly inserted student's data
        student = db.execute("SELECT * FROM students WHERE email = ?", email)
        
        
        # Assign the user_id to the session
        session["user_id"] = student[0]["id"]
        
        
        # Redirect user to login page
        return redirect(url_for("login"))
    
    # if user request is get
    return render_template("signup.html")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    # Clear session data
    session.clear()
    
    # If request method is POST then
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check the user input 
        if not email or not password:
            flash_message("Provide required Fields to Log In!", category='error')
            # return redirect(url_for('show_flash'))
            return
        
        # Check if the email already exits
        student = db.execute("SELECT * FROM students WHERE email = ?", email)
        
        # Validate the user email and password
        if not student or not (check_password_hash(student[0]["password"], password) if student else True):
            flash_message("Invalid email or password!", category='error')
            # return redirect(url_for('show_flash'))
            return
        
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
    # session["user_id"] = None
    return redirect("/login")

@app.route("/assign")
@login_required
def assign():
    return redirect(url_for("login"))


@app.route("/show_flash")
def show_flash():
    return render_template('show_flash.html')


if __name__ == '__main__':
    app.run(debug=True)