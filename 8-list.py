employee_skills = ["Python", "Java", "C++", "SQL", "JavaScript"]

while True:
    print("\nEmployee Skills Management System")
    print("1. Display Skills")
    print("2. Add Skill")
    print("3. Insert Skill")
    print("4. Update Skill")
    print("5. Remove Skill")
    print("6. Search Skill")
    print("7. Count Skills")
    print("8. Display Skills by Enumerate")
    print("9. Exit")   

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEmployee Skills:")
        for skill in employee_skills:
            print(skill)

    elif choice == 2:
        skill = input("Enter skill to add: ")
        employee_skills.append(skill)
        print("Skill added successfully!")

    elif choice == 3:
        index = int(input("Enter index: "))
        skill = input("Enter skill to insert: ")
        employee_skills.insert(index, skill)
        print("Skill inserted successfully!")

    elif choice == 4:
        index = int(input("Enter index to update: "))
        skill = input("Enter new skill: ")
        employee_skills[index] = skill
        print("Skill updated successfully!")
    elif choice == 5:
        skill = input("Enter skill to remove: ")
        if skill in employee_skills:
            employee_skills.remove(skill)
            print("Skill removed successfully!")
        else:
            print("Skill not found!")
    elif choice == 6:
        skill = input("Enter skill to search: ")
        if skill in employee_skills:
            print("Skill found!")
        else:
            print("Skill not found!")
    elif choice == 7:
        print(f"Total skills: {len(employee_skills)}")
    
    elif choice ==8:
        print("\nEmployee Skills with Index:")
        for index, skill in enumerate(employee_skills,start=0):
            print(index, "-", skill)

    elif choice == 9:
        print("Thank You!")
        break

    else:
        print("Option not implemented yet.")