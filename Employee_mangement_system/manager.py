from file_handler import append_file, read_file
from utils import *

###############################
# Adding New Employee By Manager
###############################

def add_employee():
    print("\n=== Add Employee ===")

    # ID
    while True:
        user_id = input("Enter ID (or 'exit' to cancel): ").strip()

        if user_id.lower() == "exit":
            print("Operation Cancelled!!!")
            return

        if not is_valid_id(user_id, "employee.txt"):
            continue

        if not is_duplicate_id("employee.txt", user_id):
            break

        print("ID already exists. Try again.")

    # NAME
    while True:
        name = input("Enter Name (or 'exit' to cancel): ").strip()

        if name.lower() == "exit":
            print("Operation Cancelled!!!")
            return

        if is_valid_name(name):
            break

    # EMAIL
    while True:
        email = input("Enter Email (or 'exit' to cancel): ").strip()

        if email.lower() == "exit":
            print("Operation Cancelled!!!")
            return

        if not is_valid_email(email):
            continue

        if is_duplicate_email("employee.txt", email):
            print("Email already exists")
        else:
            break

    # PASSWORD
    while True:
        password = input("Enter Password (or 'exit' to cancel): ").strip()

        if password.lower() == "exit":
            print("Operation Cancelled!!!")
            return

        if is_valid_password(password):
            break

    # SALARY
    while True:
        salary = input("Enter Salary (or 'exit' to cancel): ").strip()

        if salary.lower() == "exit":
            print("Operation Cancelled!!!")
            return

        if is_valid_salary(salary):
            break

    # ADDRESS
    address = input("Enter Address (or 'exit' to cancel): ").strip()

    if address.lower() == "exit":
        print("Operation Cancelled!!!")
        return

    append_file(
        "employee.txt",
        f"{user_id}|{name}|{email}|{password}|Employee|{salary}|{address}"
    )

    print("Employee added successfully")


###############################
# Viewing Employees 
###############################

def view_file(file):
    print("\n====== EMPLOYEE RECORDS ======")

    lines = read_file(file)

    if not lines:
        print("No records found.")
        return

    print("--------------------------------------------------------------------------------")
    print(f"{'ID':<10} {'Name':<20} {'Email':<25} {'Salary':<10}")
    print("--------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")
        print(f"{data[0]:<10} {data[1]:<20} {data[2]:<25} {data[5]:<10}")

    print("--------------------------------------------------------------------------------")
    print()
    input("Press Enter to go back to Menu")


##################################
# Viewing Enquiries 
##################################

def view_enquiries():
    print("\n========== ENQUIRIES ==========")

    lines = read_file("enquiry.txt")

    if not lines:
        print("No enquiries found.")
        return

    print("--------------------------------------------------------------------------------")
    print(f"{'Emp ID':<10} {'Enquiry':<40} {'Date':<25}")
    print("--------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")
        print(f"{data[0]:<10} {data[1]:<40} {data[2]:<25}")

    print("--------------------------------------------------------------------------------")
    print()
    input("Press Enter to go back to Menu")


####################################
# Viewing Suggestions 
####################################

def view_suggestions():
    print("\n========== SUGGESTIONS ==========")

    lines = read_file("suggestion.txt")

    if not lines:
        print("No suggestions found.")
        return

    print("--------------------------------------------------------------------------------")
    print(f"{'Emp ID':<10} {'Suggestion':<40} {'Date':<25}")
    print("--------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")
        print(f"{data[0]:<10} {data[1]:<40} {data[2]:<25}")

    print("--------------------------------------------------------------------------------")
    print()
    input("Press Enter to go back to Menu")


###############################
# Manager Menu
###############################

def manager_menu(user):
    print(f"\nWelcome, {user[1]} ({user[4]})")

    while True:
        print("\n========== MANAGER PANEL ==========")
        print("1. View Profile")
        print("2. Add Employee")
        print("3. View Employees")
        print("4. Search Employee")
        print("5. Delete Employee")
        print("6. Edit Profile")
        print("7. View Enquiries")
        print("8. View Suggestions")
        print("9. Logout")
        print("===================================")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_profile(user)

        elif choice == "2":
            add_employee()

        elif choice == "3":
            view_file("employee.txt")

        elif choice == "4":
            search_user("employee.txt")

        elif choice == "5":
            delete_user("employee.txt")

        elif choice == "6":
            edit_profile("manager.txt", user)

        elif choice == "7":
            view_enquiries()

        elif choice == "8":
            view_suggestions()

        elif choice == "9":
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please select between 1-9.")