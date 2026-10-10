# ============================================================
# Medium Project: User Management System
# ============================================================

import time

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def display_user(self):
        print(f"Name: {self.first_name} {self.last_name} | Email: {self.email}")

def create_user():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    return User(first_name, last_name, email, password)

users_list = []

while True:
    print("\nWelcome to User Management")
    print("Choose an action:")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_user = create_user()
        users_list.append(new_user)
        print("\nUser added successfully!")
        time.sleep(1)
    elif choice == '2':
        if not users_list:
            print("\nNo users found.")
        else:
            print("\n--- Users List ---")
            for user in users_list:
                user.display_user()
    elif choice == '3':
        print("\nExiting program... Goodbye!")
        break
    else:
        print("\nInvalid choice. Try again.")
