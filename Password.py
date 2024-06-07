import re

def Test(password):
    # Check length
    if len(password) < 10:
        return "Password is too short, it should be at least 10 characters long."
    
    # Check for consecutive identical characters
    if re.search(r'(.)\1\1', password):
        return "Password should not contain more than 2 identical characters in a row."
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Password should contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Password should contain at least one lowercase letter."
    
    # Check for numbers
    if not re.search("[0-9]", password):
        return "Password should contain at least one number."
    
    # Check for special characters
    if not re.search("[!@#$%^&*()-_+=]", password):
        return "Password should contain at least one special character."
    
    return "Password is strong."

password = input("Enter your password: ")
result = Test(password)
print(result)