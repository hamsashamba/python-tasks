import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@acharya\.ac\.in$' 
    return bool(re.match(pattern, email))

email = input("Enter an email to validate: ")

if is_valid_email(email):
    print(f"{email} is a valid Acharya email!")
else:
    print(f"{email} is NOT a valid Acharya email!")