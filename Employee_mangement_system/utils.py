from file_handler import append_file

###############################
# Email Validation
###############################

def is_valid_email(email):
    email = email.strip()
    if email.endswith("@gmail.com"):
        return True
    print("Invalid email! Use @gmail.com")
    return False

###############################
# Displaying the Users
###############################

def display_user(line):
    data = line.strip().split("|")
    print(f"================================")
    print(f"Name        : {data[1]}")
    print(f"ID          : {data[0]}")
    print(f"Email       : {data[2]}")
    print(f"Designation : {data[4]}")
    print(f"Salary      : {data[5]}")
    print(f"Address     : {data[6]}")
    print(f"================================")

###############################
# Viewing Own Profile
###############################

def view_profile(user):
    print("\n--- Your Profile ---")
    display_user("|".join(user))
    print()
    input("Press ENTER to go back to menu....")
    print()

###############################
# Salary Validation
###############################

def is_valid_salary(salary):
    if not salary.isdigit():
        print("Salary must be a number (Positive integer only)")
        return False

    if int(salary) < 15000:
        print("Salary must be at least 15000")
        return False

    return True

###############################
# Password Validation
###############################

def is_valid_password(password):
    password = password.strip()
    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if len(password) < 6:
        print("Password must be at least 6 characters")
        return False

    if not any(c.isalpha() for c in password):
        print("Password must contain a letter")
        return False

    if not any(c.isdigit() for c in password):
        print("Password must contain a number")
        return False

    if not any(c in special for c in password):
        print("Password must contain a special character")
        return False

    return True

###############################
# ID Format Validation
###############################

def is_valid_id(user_id, file):
    if file == "boss.txt" and not user_id.startswith("B"):
        print("Invalid ID format. Boss ID should start from B (e.g. B001)")
        return False

    if file == "manager.txt" and not user_id.startswith("M"):
        print("Invalid ID format. Manager ID should start from M (e.g. M001)")
        return False

    if file == "employee.txt" and not user_id.startswith("E"):
        print("Invalid ID format. Employee ID should start from E (e.g. E001)")
        return False

    return True

###############################
# Duplicate ID Checking
###############################

def is_duplicate_id(file, user_id):
    user_id = user_id.strip()
    for line in open(file):
        if line.split("|")[0] == user_id:
            return True
    return False

###############################
# Duplicate Email Checking
###############################

def is_duplicate_email(file, email):
    for line in open(file):
        if line.strip().split("|")[2] == email.strip():
            return True
    return False

###############################
# Searching Users
###############################

def search_user(file):
    print()
    print("If name is used to search Please use full name...")
    print()
    key = input("Enter ID/Name/Email (or 'exit' to cancel): ").strip()

    if key.lower() == "exit":
        print("Operation Cancelled!!!")
        return

    key = key.lower()
    found = False

    for line in open(file):
        if key in line.lower():
            display_user(line)
            found = True

    if not found:
        print("No record found")

###############################
# Deleting User
###############################

def delete_user(file):
    key = input("Enter ID to delete (or 'exit' to cancel): ").strip()

    if key.lower() == "exit":
        print("Operation Cancelled!!!")
        return

    lines = open(file).readlines()

    found = any(line.startswith(key + "|") for line in lines)

    if not found:
        print("User not found")
        return

    confirm = input("Are you sure you want to delete this user? (yes/no): ").lower()

    if confirm != "yes":
        print("Cancelled")
        return

    with open(file, "w") as f:
        for line in lines:
            if not line.startswith(key + "|"):
                f.write(line)

    print("User deleted successfully")

###############################
# Editing Personal Profile
###############################

def edit_profile(file, user):
    lines = open(file).readlines()
    new_data = []

    print("\n--- Current Profile ---")

    for line in lines:
        data = line.strip().split("|")
        if data[0] == user[0]:
            display_user(line)

    print("\n--- Enter New Details ---")

    old_name = user[1]
    old_email = user[2]
    old_password = user[3]
    old_address = user[6]

    # Name
    while True:
        new_name = input("New Name (or 'exit' to cancel): ").strip()

        if new_name.lower() == "exit":
            print("Operation cancelled")
            return

        if new_name == old_name:
            print("New name cannot be same as previous name")
            continue

        if is_valid_name(new_name):
            name = new_name
            break

    # Email (NOT editable)
    print(f"Email (cannot be changed): {old_email}")
    email = old_email

    # Password
    while True:
        password_input = input("New Password (or 'exit' to cancel): ").strip()

        if password_input.lower() == "exit":
            print("Operation cancelled")
            return

        if password_input == old_password:
            print("New password cannot be same as previous password")
            continue

        if is_valid_password(password_input):
            password = password_input
            break

    # Address
    while True:
        address_input = input("New Address (or 'exit' to cancel): ").strip()

        if address_input.lower() == "exit":
            print("Operation cancelled")
            return

        if address_input == old_address:
            print("New address cannot be same as previous address")
            continue

        address = address_input
        break

    # Update file
    for line in lines:
        data = line.strip().split("|")

        if data[0] == user[0]:
            updated = f"{data[0]}|{name}|{email}|{password}|{data[4]}|{data[5]}|{address}\n"
            new_data.append(updated)
        else:
            new_data.append(line)

    open(file, "w").writelines(new_data)

    print("Profile updated successfully")

###############################
# Editing Any User (Boss)
###############################

def edit_any_user(file):
    user_id = input("Enter ID to edit (or 'exit' to cancel): ").strip()

    if user_id.lower() == "exit":
        print("Operation Cancelled!!!")
        return

    lines = open(file).readlines()
    new_data = []
    found = False

    for line in lines:
        data = line.strip().split("|")

        if data[0] == user_id:
            found = True

            print("\n--- Current Details ---")
            display_user(line)

            name, email, password, designation, salary, address = data[1], data[2], data[3], data[4], data[5], data[6]

            while True:
                print("\n--- What do you want to edit? ---")
                print("1. Name")
                print("2. Email (Not Editable)")
                print("3. Password")
                print("4. Designation")
                print("5. Salary")
                print("6. Address")
                print("7. Save & Exit")

                choice = input("Enter choice (or 'exit' to cancel): ").strip()

                if choice.lower() == "exit":
                    print("Operation Cancelled!!!")
                    return

                #  NAME
                if choice == "1":
                    while True:
                        new_name = input("New Name: ").strip()

                        if new_name == name:
                            print("New name cannot be same as previous")
                            continue

                        if is_valid_name(new_name):
                            name = new_name
                            break

                #  EMAIL (LOCKED)
                elif choice == "2":
                    print(f"Email cannot be changed: {email}")

                #  PASSWORD
                elif choice == "3":
                    while True:
                        new_pass = input("New Password: ").strip()

                        if new_pass == password:
                            print("New password cannot be same as previous")
                            continue

                        if is_valid_password(new_pass):
                            password = new_pass
                            break

                #  DESIGNATION CHANGE
                elif choice == "4":
                    while True:
                        print("\nChange Designation:")
                        print("1. Manager")
                        print("2. Employee")
                        print("3. Cancel")

                        choice_2 = input("Enter choice: ").strip()

                        if choice_2 == "1":
                            if designation == "Manager":
                                print("Already a Manager")
                                break
                            designation = "Manager"
                            break

                        elif choice_2 == "2":
                            if designation == "Employee":
                                print("Already an Employee")
                                break
                            designation = "Employee"
                            break

                        elif choice_2 == "3":
                            print("Operation Cancelled!!!")
                            break

                        else:
                            print("Invalid choice!!!")

                #  SALARY
                elif choice == "5":
                    while True:
                        new_salary = input("New Salary: ").strip()

                        if new_salary == salary:
                            print("New salary cannot be same as previous")
                            continue

                        if is_valid_salary(new_salary):
                            salary = new_salary
                            break

                #  ADDRESS
                elif choice == "6":
                    new_address = input("New Address: ").strip()

                    if new_address == address:
                        print("New address cannot be same as previous")
                    else:
                        address = new_address

                #  SAVE
                elif choice == "7":
                    break

                else:
                    print("Invalid choice!!!!")

            #  AUTO CHANGE ID BASED ON DESIGNATION
            old_id = data[0]

            if designation == "Manager":
                new_id = "M" + old_id[1:]
            else:
                new_id = "E" + old_id[1:]

            updated_line = f"{new_id}|{name}|{email}|{password}|{designation}|{salary}|{address}\n"

            #  SAME FILE UPDATE
            if (file == "manager.txt" and designation == "Manager") or \
               (file == "employee.txt" and designation == "Employee"):

                new_data.append(updated_line)

            else:
                #  MOVE TO OTHER FILE
                if designation == "Manager":
                    append_file("manager.txt", updated_line.strip())
                else:
                    append_file("employee.txt", updated_line.strip())

            continue  # skip old record

        else:
            new_data.append(line)

    open(file, "w").writelines(new_data)

    if found:
        print("User updated successfully")
    else:
        print("User not found")
        
###############################
# Name Validation
###############################

def is_valid_name(name):
    if name.replace(" ", "").isalpha():
        return True
    print("Name must contain only alphabets")
    return False

###############################
# Enquiry/Suggestion Validation
###############################

def is_valid_text(text):

    if text == "":
        print("Text cannot be empty")
        return False

    if not text[0].isalpha():
        print("Text must start with a letter")
        return False

    if len(text) < 10:
        print("Text must be at least 10 characters long")
        return False

    digit_count = sum(c.isdigit() for c in text)

    if digit_count > 10:
        print("Text cannot contain more than 10 numeric values")
        return False

    return True