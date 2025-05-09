import hashlib
user_data = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists! Try a different one.")
        return

    password = input("Enter a password: ")
    user_data[username] = hash_password(password)
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    if username not in user_data:
        print("Username not found! Please register.")
        return

    password = input("Enter your password: ")
    if user_data[username] == hash_password(password):
        print("Login successful! Welcome", username)
    else:
        print("Incorrect password! Try again.")

while True:
    print("\nUser Authentication System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option! Please enter 1, 2, or 3.")