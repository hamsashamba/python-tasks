user_data = []

def addUser():
    user_id = int(input("Enter User ID: "))
    if any(user["ID"] == user_id for user in user_data):
        print(f"Error: User ID {user_id} already exists! Try again with different user ID")
        return
    name = input("Enter Name: ")
    email = input("Enter Email ID: ")
    user_data.append({"ID": user_id, "Name": name, "Email_ID": email})
    print(f"User {name} added successfully!")

def getUser():
    user_id = int(input("Enter User ID to retrieve: "))
    for user in user_data:
        if user["ID"] == user_id:
            print("User Found: ", user)
            return
    print("User not found!")

def updateUser():
    user_id = int(input("Enter User ID to update: "))
    for user in user_data:
        if user["ID"] == user_id:
            name = input(f"Enter new name (press Enter to keep '{user['Name']}'): ") or user["Name"]
            email = input(f"Enter new email ID (press Enter to keep '{user['Email_ID']}'): ")
            if email: user["Email_ID"] = email
            user["Name"] = name
            print(f"User {user_id} updated successfully!")
            return
    print("User not found!")

def deleteUser():
    user_id = int(input("Enter User ID to delete: "))
    for i, user in enumerate(user_data):
        if user["ID"] == user_id:
            del user_data[i]
            print(f"User {user_id} deleted successfully!")
            return
    print("User not found!")

def displayUsers():
    if user_data:
        for user in user_data:
            print(user)
    else:
        print("No users available!")

while True:
    print("\nCRUD Operations Menu:")
    print("1. Add User")
    print("2. Retrieve User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Display All Users")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        addUser()
    elif choice == "2":
        getUser()
    elif choice == "3":
        updateUser()
    elif choice == "4":
        deleteUser()
    elif choice == "5":
        displayUsers()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
