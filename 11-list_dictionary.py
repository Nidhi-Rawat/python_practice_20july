MRU = {}
MRIIRS = {}

def add_student():
    college = input("Enter College (MRU/MRIIRS): ").upper()

    key = int(input("Enter Student Key: "))

    if key in MRU or key in MRIIRS:
        print("Key Already Assigned!")
        return

    roll = int(input("Enter Roll No: "))
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")

    if college == "MRU":
        MRU[key] = [roll, name, branch]
        print("Student Added Successfully in MRU.")

    elif college == "MRIIRS":
        MRIIRS[key] = [roll, name, branch]
        print("Student Added Successfully in MRIIRS.")

    else:
        print("Invalid College!")


def view_students():

    print("\n========== MRU ==========")
    if not MRU:
        print("No Students Found")
    else:
        for key, details in MRU.items():
            print(f"Key : {key}")
            print(f"Roll No : {details[0]}")
            print(f"Name : {details[1]}")
            print(f"Branch : {details[2]}")
            print()

    print("\n========== MRIIRS ==========")
    if not MRIIRS:
        print("No Students Found")
    else:
        for key, details in MRIIRS.items():
            print(f"Key : {key}")
            print(f"Roll No : {details[0]}")
            print(f"Name : {details[1]}")
            print(f"Branch : {details[2]}")
            print()


def search_student():

    key = int(input("Enter Student Key: "))

    if key in MRU:
        print("\nStudent Found in MRU")
        print(MRU[key])

    elif key in MRIIRS:
        print("\nStudent Found in MRIIRS")
        print(MRIIRS[key])

    else:
        print("Student Not Found")


while True:

    print("\n============== Student Management ==============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")