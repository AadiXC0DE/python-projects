def check_password_strength(password):
    # Define the criteria for a strong password
    length = len(password) >= 8  # Minimum length of 8 characters
    uppercase = any(char.isupper() for char in password)  # At least one uppercase letter
    lowercase = any(char.islower() for char in password)  # At least one lowercase letter
    digit = any(char.isdigit() for char in password)  # At least one digit
    special_char = any(char in '!@#$%^&*(),.?":{}|<>' for char in password)  # At least one special character


    if not password:
        return "Invalid"
    elif length and uppercase and lowercase and digit and special_char:
        return "Very Strong"
    elif length and uppercase and lowercase and digit:
        return "Strong"
    elif length and uppercase and lowercase:
        return "Moderate"
    elif length >= 8:
        return "Weak"
    else:
        return "Very Weak"


password = input("Enter a password: ")

# Check the strength of the password
strength = check_password_strength(password)
print("Password strength:", strength)
