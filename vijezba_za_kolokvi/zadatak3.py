import re

def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$%*?&!])[A-Za-z\d@$%*?&!]{9,}$"
    
    if re.match(pattern, password):
        return True
    else:
        return False

password = "Password123!"
if validate_password(password):
    print("Lozinka je dobra")
else:
    print("Fali ti nesto :)")
