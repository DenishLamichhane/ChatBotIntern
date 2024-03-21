# ValidationUtils.py

import re

def validate_email(email):
    """
    Validates the format of an email address.
    
    Parameters:
    - email (str): The email address to be validated.
    
    Returns:
    - bool: True if the email address has a valid format, False otherwise.
    """
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def validate_phone(phone):
    """
    Validates the format of a phone number.
    
    Parameters:
    - phone (str): The phone number to be validated.
    
    Returns:
    - bool: True if the phone number has a valid format, False otherwise.
    """
    return phone.isdigit() and len(phone) == 10
