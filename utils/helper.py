import os
import sys
import re
import logging
from datetime import datetime
import bcrypt
from tkinter import messagebox

# === Path Utilities ===
def resource_path(relative_path):
    """ Get the absolute path to a resource (works for dev and PyInstaller) """
    try:
        # PyInstaller creates a temp folder
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# === Validation Utilities ===
def validate_email(email):
    """ Validate email format """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """ Validate phone number (10 digits) """
    return re.match(r"^\d{10}$", phone) is not None

def validate_date(date_str):
    """ Validate date format (YYYY-MM-DD) """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# === Password Utilities ===
def hash_password(password):
    """ Hash a password using bcrypt """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(plain_password, hashed_password):
    """ Verify a password against a hash """
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

# === Date Utilities ===
def get_current_date():
    """ Return current date in YYYY-MM-DD format """
    return datetime.now().strftime("%Y-%m-%d")

def calculate_nights(check_in, check_out):
    """ Calculate number of nights between two dates """
    delta = datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")
    return delta.days

# === Logging Utilities ===
def setup_logger():
    """ Configure application logging """
    logging.basicConfig(
        filename=resource_path("logs/suite_spot.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# === Error Handling ===
def show_error(message):
    """ Display a Tkinter error message """
    messagebox.showerror("Error", message)

# === Database Utilities ===
def initialize_database():
    """ Initialize the database schema if it doesn't exist """
    from database.db import get_db_connection  # Avoid circular imports
    try:
        with open(resource_path("database/schema.sql"), "r") as f:
            schema = f.read()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(schema)
        conn.commit()
    except Exception as e:
        logging.error(f"Database initialization failed: {str(e)}")
        raise