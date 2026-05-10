import os

###############################
# Checking if file is empty
###############################

def is_file_empty(file):
    if not os.path.exists(file):
        return True

    with open(file, "r") as f:
        return len(f.read().strip()) == 0


###################################
# Creating files if they don't exist
###################################

def create_files():

    files = [
        "boss.txt",
        "manager.txt",
        "employee.txt",
        "enquiry.txt",
        "suggestion.txt"
    ]

    for file in files:
        if not os.path.exists(file):
            open(file, "w").close()


###############################
# Reading data inside the file
###############################

def read_file(file):

    if not os.path.exists(file):
        return []

    with open(file, "r") as f:
        return f.readlines()


###############################
# Writing data inside the file
###############################

def write_file(file, lines):

    with open(file, "w") as f:
        f.writelines(lines)


###############################
# Appending data in the file
###############################

def append_file(file, data):

    with open(file, "a") as f:
        f.write(data + "\n")


###############################
# View Employees Enquiries 
###############################

def view_enquiries():

    print("\n========== ENQUIRIES ==========")

    lines = read_file("enquiry.txt")

    if not lines:
        print("No enquiries found.")
        return

    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(f"{'Employee ID':<15} {'Enquiry':<50} {'Date'}")
    print("----------------------------------------------------------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")

        # Safety check (avoid crash if data is incomplete)
        if len(data) < 3:
            continue

        print(f"{data[0]:<15} {data[1]:<40} {data[2]}")

    print("----------------------------------------------------------------------------------------------------------------------------------")
    print()
    input("Press Enter to go back to Menu")


###############################
# View Employees Suggestions 
###############################

def view_suggestions():

    print("\n========== SUGGESTIONS ==========")

    lines = read_file("suggestion.txt")

    if not lines:
        print("No suggestions found.")
        return

    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(f"{'Employee ID':<15} {'Suggestion':<50} {'Date'}")
    print("----------------------------------------------------------------------------------------------------------------------------------")

    for line in lines:
        data = line.strip().split("|")

        # Safety check
        if len(data) < 3:
            continue

        print(f"{data[0]:<15} {data[1]:<40} {data[2]}")

    print("----------------------------------------------------------------------------------------------------------------------------------")
    print()
    input("Press Enter to go back to Menu...")