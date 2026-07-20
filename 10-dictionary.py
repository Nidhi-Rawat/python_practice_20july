MRU = {
    1: [101, "Nidhi", "CSE"],
    2: [102, "Rahul", "IT"]
}

MRIIRS = {
    3: [201, "Shagun", "ECE"],
    4: [202, "Ankit", "MBA"]
}


def add_student():
    college = input("Enter College (MRU/MRIIRS): ").upper()

    key = int(input("Enter Key: "))

    if key in MRU or key in MRIIRS:
        print("Key Already Assigned!")
        return

    roll = int(input("Enter Roll No: "))
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")

    if college == "MRU":
        MRU[key] = [roll, name, branch]
        print("Student Added to MRU")

    elif college == "MRIIRS":
        MRIIRS[key] = [roll, name, branch]
        print("Student Added to MRIIRS")

    else:
        print("Invalid College")


def view_students():

    print("\n----- MRU Students -----")
    for key, details in MRU.items():
        print("Key:", key)
        print("Roll No:", details[0])
        print("Name:", details[1])
        print("Branch:", details[2])
        print()

    print("----- MRIIRS Students -----")
    for key, details in MRIIRS.items():
        print("Key:", key)
        print("Roll No:", details[0])
        print("Name:", details[1])
        print("Branch:", details[2])
        print()


def search_student():
    key = int(input("Enter Key to Search: "))

    if key in MRU:
        print("Student Found in MRU")
        print("Roll No:", MRU[key][0])
        print("Name:", MRU[key][1])
        print("Branch:", MRU[key][2])

    elif key in MRIIRS:
        print("Student Found in MRIIRS")
        print("Roll No:", MRIIRS[key][0])
        print("Name:", MRIIRS[key][1])
        print("Branch:", MRIIRS[key][2])

    else:
        print("Student Not Found")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")