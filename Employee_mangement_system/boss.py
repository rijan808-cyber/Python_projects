from file_handler import append_file, read_file, view_enquiries, view_suggestions
from utils import *

################################
# For Viewing Managers 
################################

def view_managers():
    print("\n====== MANAGERS ======")

    lines = read_file("manager.txt")

    if not lines:
        print("No managers created")
        return

    print("--------------------------------------------------------------------------------")
    print(f"{'ID':<10} {'Name':<20} {'Email':<25} {'Salary':<10}")
    print("--------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")
        print(f"{data[0]:<10} {data[1]:<20} {data[2]:<25} {data[5]:<10}")

    print("--------------------------------------------------------------------------------")
    print()
    input("Press ENTER to go back to Boss Menu....")


################################
# For Viewing Employees 
################################

def view_employees():
    print("\n====== EMPLOYEES ======")

    lines = read_file("employee.txt")

    if not lines:
        print("No employees created")
        return

    print("--------------------------------------------------------------------------------")
    print(f"{'ID':<10} {'Name':<20} {'Email':<25} {'Salary':<10}")
    print("--------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")
        print(f"{data[0]:<10} {data[1]:<20} {data[2]:<25} {data[5]:<10}")

    print("--------------------------------------------------------------------------------")
    print()
    input("Press ENTER to go back to Boss Menu...")


################################
# For Counting Users
################################

def show_counts():
    managers = read_file("manager.txt")
    employees = read_file("employee.txt")

    print("\n====== SYSTEM SUMMARY ======")
    print(f"Total Managers  : {len(managers)}")
    print(f"Total Employees : {len(employees)}")

    if len(managers) == 0:
        print("No managers created")

    if len(employees) == 0:
        print("No employees created")

    print("================================")

    input("Press ENTER to go back to Boss Menu")


################################
# To Add New Employees or Manager
################################

def add_user(file):
    print("\n=== Add User ===")

    # ID INPUT
    while True:
        user_id = input("Enter ID (or 'exit' to cancel): ").strip()

        if user_id.lower() == "exit":
            print()
            print("Operation Cancelled!!!")
            return

        # ID format validation
        if not is_valid_id(user_id, file):
            continue

        if not is_duplicate_id(file, user_id):
            break

        print("ID already exists... Please use another one..")

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

        if is_duplicate_email(file, email):
            print("Email already exists Use another email")
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

    # DESIGNATION
    if file == "manager.txt":
        designation = "Manager"
    else:
        designation = "Employee"

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
        file,
        f"{user_id}|{name}|{email}|{password}|{designation}|{salary}|{address}"
    )

    print("User added successfully")


###############################
# Boss Menu
###############################

def boss_menu(user):
    print(f"\nWelcome, {user[1]} ({user[4]})")

    while True:
        print("\n========== BOSS PANEL ==========")
        print("1. Add Manager")
        print("2. Add Employee")
        print("3. View Managers")
        print("4. View Employees")
        print("5. System Summary")
        print("6. Search")
        print("7. Delete")
        print("8. View Profile")
        print("9. Edit Own Profile")
        print("10. Edit Manager")
        print("11. Edit Employee")
        print("12. View Enquiries")
        print("13. View Suggestions")
        print("14. Logout")
        print("================================")

        choice = input("ENTER choice: ").strip()

        if choice == "1":
            add_user("manager.txt")

        elif choice == "2":
            add_user("employee.txt")

        elif choice == "3":
            view_managers()

        elif choice == "4":
            view_employees()

        elif choice == "5":
            show_counts()

        elif choice == "6":
            search_user("manager.txt")
            search_user("employee.txt")

        elif choice == "7":
            delete_user("manager.txt")
            delete_user("employee.txt")

        elif choice == "8":
            view_profile(user)

        elif choice == "9":
            edit_profile("boss.txt", user)

        elif choice == "10":
            edit_any_user("manager.txt")

        elif choice == "11":
            edit_any_user("employee.txt")

        elif choice == "12":
            view_enquiries()

        elif choice == "13":
            view_suggestions()

        elif choice == "14":
            print("Logging out...")
            break

        else:
            print("Invalid choice!!!! Please select between 1-14.")