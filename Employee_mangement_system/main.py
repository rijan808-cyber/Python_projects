from file_handler import create_files, append_file, is_file_empty
from auth import login
from boss import boss_menu
from manager import manager_menu
from employee import employee_menu
from utils import *

###############################
# Create Boss if not exists
###############################

def create_boss():
    print("\nNo Boss account found. Please create one.")
    print("\n========== CREATE BOSS ACCOUNT ==========")

    # ID
    while True:
        user_id = input("Enter ID : ").strip()

        if not is_valid_id(user_id, "boss.txt"):
            continue

        if not is_duplicate_id("boss.txt", user_id):
            break

        print("ID already exists")

    # NAME
    while True:
        name = input("Enter Name : ").strip()

        if is_valid_name(name):
            break

    # EMAIL
    while True:
        email = input("Enter Email : ").strip()

        if not is_valid_email(email):
            continue

        if is_duplicate_email("boss.txt", email):
            print("Email already exists")
        else:
            break

    # PASSWORD
    while True:
        password = input("Enter Password : ").strip()

        if password.lower() == "exit":
            print("Operation cancelled")
            return

        if is_valid_password(password):
            break

    # SALARY
    while True:
        salary = input("Salary : ").strip()

        if is_valid_salary(salary):
            break

    # ADDRESS
    address = input("Enter Address : ").strip()

    append_file(
        "boss.txt",
        f"{user_id}|{name}|{email}|{password}|Boss|{salary}|{address}"
    )

    print("\nBoss account created successfully!")


###############################
# Main System
###############################

def main():
    print("\n===================================================")
    print("     WELCOME TO EMPLOYMENT MANAGEMENT SYSTEM     ")
    print("===================================================")
    print("Project Members:")
    print("• Priyanka Kumari Shah (Leader) (NP071538)")
    print("• Rijan Pariyar (NP071544)")
    print("• Aayub Gotame (NP071491)")
    print("• Abhishek Bhattrai Kshetri (NP071493)")
    print("===================================================\n")
    
    input("Press ENTER to continue...")

    ######################################
    # Create files if not exists
    ######################################
    create_files()

    ######################################
    # Create Boss if not exists
    ######################################
    if is_file_empty("boss.txt"):
        create_boss()

    ###############################
    # Main Menu
    ###############################
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Boss Login")
        print("2. Manager Login")
        print("3. Employee Login")
        print("4. Exit")
        print("================================")

        choice = input("Enter choice: ").strip()

        ################################
        # Boss Login
        ################################
        if choice == "1":
            user = login("boss.txt")
            if user:
                boss_menu(user)

        ################################
        # Manager Login
        ################################
        elif choice == "2":
            user = login("manager.txt")
            if user:
                manager_menu(user)

        ################################
        # Employee Login
        ################################
        elif choice == "3":
            user = login("employee.txt")
            if user:
                employee_menu(user)

        ################################
        # Exit
        ################################
        elif choice == "4":
            print("\nThank you for using the system.")
            print("Goodbye!")
            break

        ################################
        # Invalid Input
        ################################
        else:
            print("Invalid choice. Please select between 1-4.")


###############################
# Run Program
###############################

main()