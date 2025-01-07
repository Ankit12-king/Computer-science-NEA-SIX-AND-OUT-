import re
def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

   
    if re.search(r"\s", password):
        return "Password must not contain spaces."

    return "Password is valid."

password = input("Enter your password: ")
result = check_password(password)
print(result)
