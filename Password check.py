import re

def check_password_strength(password):
#Rule checks
    min_length = 10
    length_error = len(password) < min_length
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*-_=+{ };:]", password) is None
    
#Result handling if error
    errors = {
        "Does not meet length requirement": length_error,
        "No uppercase alphabet detected": uppercase_error,
        "No lowercase alphabet detected": lowercase_error,
        "No digit detected": digit_error,
        "No special character detected": special_char_error
        }
    
#If no error
    if not any(errors.values()):
        return "Password viable"
    else:
        result = "Password is insecure. Issues:\n"
        for issue, failed in errors.items():
            if failed:
                result += f"    - {issue}\n"
#End of function
    return result


#Testing passsword
password = input("Enter a password to check: ")
print(check_password_strength(password))