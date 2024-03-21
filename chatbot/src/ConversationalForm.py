# ConversationalForm.py

# Sample function to collect user information through a conversational form
def collect_user_info():
    user_info = {}
    
    # Define conversation flow
    prompts = {
        "name": "May I know your name?",
        "phone": "Could you please provide your phone number?",
        "email": "What's your email address?"
    }
    
    # Loop through prompts and collect information
    for key, prompt in prompts.items():
        print(prompt)
        user_input = input().strip()
        user_info[key] = user_input
    
    return user_info

# Sample function to validate email format
def validate_email(email):
    # Implement your email validation logic here
    # This is a simple example using regex
    import re
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# Sample function to validate phone number format
def validate_phone(phone):
    # Implement your phone number validation logic here
    # This is a simple example checking for digits and length
    return phone.isdigit() and len(phone) == 10

# Sample function to manage conversation state
def manage_conversation():
    user_info = {}
    
    # Collect user information
    user_info = collect_user_info()
    
    # Validate email and phone number
    while not validate_email(user_info["email"]):
        print("Invalid email format. Please provide a valid email address.")
        user_info["email"] = input().strip()
    
    while not validate_phone(user_info["phone"]):
        print("Invalid phone number format. Please provide a valid phone number.")
        user_info["phone"] = input().strip()
    
    # Display collected information
    print("Collected information:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

# Sample function to initiate conversational form for user information collection
def initiate_conversational_form():
    print("Welcome! Let's collect some information.")
    manage_conversation()

# Call the function to initiate the conversational form
if __name__ == "__main__":
    initiate_conversational_form()
