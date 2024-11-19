import re

# Predefined list of common weak passwords (this can be expanded)
common_passwords = [
    '123456', 'password', '12345678', 'qwerty', 'abc123', 'password1', '12345', 
    'letmein', 'welcome', 'admin', 'football', 'monkey', 'login', 'access'
]

def check_password_strength(password):
    weaknesses = []
    recommendations = []

    # 1. Check password length
    if len(password) < 8:
        weaknesses.append("Password is too short. It should be at least 8 characters.")
        recommendations.append("Use a password with at least 12-16 characters for better security.")
    
    # 2. Check for variety of characters (lowercase, uppercase, digits, symbols)
    if not re.search("[a-z]", password):
        weaknesses.append("Password does not contain any lowercase letters.")
        recommendations.append("Include lowercase letters (a-z).")
    if not re.search("[A-Z]", password):
        weaknesses.append("Password does not contain any uppercase letters.")
        recommendations.append("Include uppercase letters (A-Z).")
    if not re.search("[0-9]", password):
        weaknesses.append("Password does not contain any digits.")
        recommendations.append("Include numbers (0-9).")
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        weaknesses.append("Password does not contain any special characters.")
        recommendations.append("Include special characters (e.g., !@#$%^&*).")
    
    # 3. Check if the password is a common password
    if password in common_passwords:
        weaknesses.append("Password is too common and easy to guess.")
        recommendations.append("Avoid common passwords like '123456', 'password', etc.")
    
    # 4. Check if the password contains sequences or repetition
    if re.search(r"(.)\1{2,}", password):  # Looks for 3 or more repeated characters
        weaknesses.append("Password contains repeated characters.")
        recommendations.append("Avoid repeated characters.")
    if re.search(r"(123|abc|qwerty|password)", password, re.IGNORECASE):
        weaknesses.append("Password contains a sequence or common phrase.")
        recommendations.append("Avoid predictable patterns like '123', 'abc', or 'qwerty'.")

    # 5. If no weaknesses were found, the password is considered strong
    if not weaknesses:
        print("Your password is strong!")
        return
    
    # Output the results
    print("Weaknesses detected in your password:")
    for weakness in weaknesses:
        print(f" - {weakness}")
    
    print("\nRecommendations to improve your password:")
    for recommendation in recommendations:
        print(f" - {recommendation}")

# Example usage
password = input("Enter your password to evaluate: ")
check_password_strength(password)
