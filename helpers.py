# helpers.py
from flask import session, redirect, flash, url_for, render_template
from functools import wraps
from cs50 import SQL
import secrets, re
import random

def flash_message(message, category='default'):
    # flash(message, category=category)
    flash((message, category), category=category)

def check_required_fields(fields, current_page):
    missing_fields = [field for field, value in fields.items() if not value]
    
    # If fields missing then show message
    if missing_fields:
        for field in missing_fields:
            flash_message(f"{field.capitalize()} is required.", category='error')
        return render_template(f"{current_page}.html")
    
    # Give us None in return if all good
    return None


def validate_class_name(class_name):
    # Validate Class Name using a regular expression
    class_name_pattern = re.compile(r'^[A-Za-z0-9_\-]+$')
    
    return class_name_pattern.match(class_name)


# login required function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# Generating secret key for session
def generate_secret_key(length=32):
    return secrets.token_hex(length // 2)


# Query data from database
def get_new_study_materials(db, session):
    """Fetch study materials from the database."""
    # Fetch all study materials from the database
    all_study_materials = db.execute('SELECT * FROM study_materials')
    
    # Get the list of materials already shown
    shown_materials = session.get('shown_materials', [])
     # Find unique materials that haven't been shown
    unique_materials = [material for material in all_study_materials if material['id'] not in shown_materials]

    # If all materials have been shown, reset the list
    if not unique_materials:
        shown_materials.clear()

    # Choose a random set of materials
    random.shuffle(unique_materials)
    selected_materials = unique_materials[:6]

    # Update the list of shown materials in the session
    shown_materials.extend(material['id'] for material in selected_materials)
    session['shown_materials'] = shown_materials

    return selected_materials