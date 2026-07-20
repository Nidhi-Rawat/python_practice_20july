employees = []

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        designation = input("Enter Designation: ")

        employee = {
            "ID": emp_id,
            "Name": name,
            "Salary": salary,
            "Designation": designation
        }

        employees.append(employee)
        print("Employee Added Successfully!")

    elif choice == 2:
        print("\nEmployee Details")
        for emp in employees:
            print("ID          :", emp["ID"])
            print("Name        :", emp["Name"])
            print("Salary      :", emp["Salary"])
            print("Designation :", emp["Designation"])

    elif choice == 3:
        search = input("Enter Employee ID to Search: ")

        found = False

        for emp in employees:
            if emp["ID"] == search:
                print("\nEmployee Found")
                print("ID          :", emp["ID"])
                print("Name        :", emp["Name"])
                print("Salary      :", emp["Salary"])
                print("Designation :", emp["Designation"])
                found = True
                break

        if not found:
            print("Employee Not Found!")

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")