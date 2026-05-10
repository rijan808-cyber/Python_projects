from file_handler import append_file
from utils import *
from datetime import datetime

###############################
# Employee Menu
###############################

def employee_menu(user):
    print(f"\nWelcome, {user[1]} ({user[4]})")

    while True:
        print("\n========== EMPLOYEE MENU ==========")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Submit Enquiry")
        print("4. Submit Suggestion")
        print("5. Logout")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        ################################
        # View Profile
        ################################
        if choice == "1":
            view_profile(user)

        ################################
        # Edit Profile
        ################################
        elif choice == "2":
            edit_profile("employee.txt", user)

        ################################
        # Enquiry Section
        ################################
        elif choice == "3":
            while True:
                text = input("Enter enquiry (or type 'exit' to cancel): ").strip()

                if text.lower() == "exit":
                    print("Operation cancelled")
                    break

                if is_valid_text(text):
                    append_file(
                        "enquiry.txt",
                        f"{user[0]}|{text}|{datetime.now()}"
                    )
                    print("Enquiry submitted successfully")
                    break

        ################################
        # Suggestion Section
        ################################
        elif choice == "4":
            while True:
                text = input("Enter suggestion (or type 'exit' to cancel): ").strip()

                if text.lower() == "exit":
                    print("Operation cancelled")
                    break

                if is_valid_text(text):
                    append_file(
                        "suggestion.txt",
                        f"{user[0]}|{text}|{datetime.now()}"
                    )
                    print("Suggestion submitted successfully")
                    break

        ################################
        # Logout
        ################################
        elif choice == "5":
            print("Logging out...")
            break

        ################################
        # Invalid Input
        ################################
        else:
            print("Invalid choice! Please select between 1-5.")