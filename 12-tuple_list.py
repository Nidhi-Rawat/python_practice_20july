employee = (
    101,
    "Nidhi Rawat",
    "CSE",
    ["Payroll System", "HR Portal"]
)


def view_employee():
    print("\n===== Employee Details =====")
    print("Employee ID :", employee[0])
    print("Employee Name :", employee[1])
    print("Department :", employee[2])
    print("Projects :", employee[3])


def add_project():
    project = input("Enter Project Name: ")
    employee[3].append(project)
    print("Project Added Successfully.")


def remove_project():
    project = input("Enter Project Name: ")

    if project in employee[3]:
        employee[3].remove(project)
        print("Project Removed Successfully.")
    else:
        print("Project Not Found.")


def search_project():
    project = input("Enter Project Name: ")

    if project in employee[3]:
        print("Project Assigned.")
    else:
        print("Project Not Assigned.")


def total_projects():
    print("Total Projects :", len(employee[3]))


def display_projects():
    print("\nProjects in Alphabetical Order")

    projects = sorted(employee[3])

    for p in projects:
        print(p)


while True:

    print("\n===== Employee Project Management System =====")
    print("1. View Employee Details")
    print("2. Add New Project")
    print("3. Remove Project")
    print("4. Search Project")
    print("5. Display Total Number of Projects")
    print("6. Display Projects Alphabetically")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        view_employee()

    elif choice == 2:
        add_project()

    elif choice == 3:
        remove_project()

    elif choice == 4:
        search_project()

    elif choice == 5:
        total_projects()

    elif choice == 6:
        display_projects()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")