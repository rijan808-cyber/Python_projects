from file_handler import read_file

############################################
# Login System with 3 Attempts
############################################

def login(file):

    attempts = 3

    while attempts > 0:

        print("\n--- LOGIN ---")

        user_id = input("Enter ID (or 'exit' to cancel): ").strip()

        if user_id.lower() == "exit":
            print()
            print("Login Cancelled!!!!")
            return None

        password = input("Enter Password: ").strip()

        lines = read_file(file)

        if not lines:
            print("No accounts found. Please contact admin/boss...")
            return None

        for line in lines:
            data = line.strip().split("|")

            if data[0] == user_id and data[3] == password:
                print("\nLogin Successful!")
                return data

        attempts -= 1
        print(f"Invalid ID or Password! Attempts left: {attempts}")

    print("\nToo many failed attempts!!! Returning to main menu...")
    return None