import re

def check_password_strength(password):
    # Define the criteria
    length = re.compile(r'.{8,}')  # Minimum length of 8 characters
    criteria = [
        (re.compile(r'[A-Z]'), "Password should contain at least one uppercase letter."),
        (re.compile(r'[a-z]'), "Password should contain at least one lowercase letter."),
        (re.compile(r'\d'), "Password should contain at least one digit."),
        (re.compile(r'[!@#$%^&*()_+\-=[\]{};:\'",.<>/?\\|]'), "Password should contain at least one special character.")
    ]

    # Check the password against the criteria

    if not length.search(password):
        return "Password should have a minimum length of 8 characters."
    
    error_messages = []
    for pattern, error_msg in criteria:
        if not pattern.search(password):
            error_messages.append(error_msg)
    
    if error_messages:
        return '\n'.join(error_messages)

    return "Password is strong."

# Test the password strength checker

password = input("Enter a password: ")
result = check_password_strength(password)
print(result)
