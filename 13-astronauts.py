astronauts = [
    (201, "Nidhi", "NASA", ["Artemis I", "Lunar Research"]),
    (202, "Vansh", "ISRO", ["Gaganyaan", "Orbital Training"]),
    (203, "Paroksh", "ESA", ["Mars Explorer", "Moon Base", "Deep Space Research"])
]


def register_astronaut():
    aid = int(input("Enter Astronaut ID: "))
    name = input("Enter Astronaut Name: ")
    agency = input("Enter Space Agency: ")

    n = int(input("Enter Number of Missions: "))
    missions = []

    for i in range(n):
        mission = input("Enter Mission Name: ")
        missions.append(mission)

    astronaut = (aid, name, agency, missions)
    astronauts.append(astronaut)

    print("Astronaut Registered Successfully.")


def view_astronauts():

    if len(astronauts) == 0:
        print("No Astronaut Found")
        return

    for astronaut in astronauts:
        print("\nAstronaut ID :", astronaut[0])
        print("Name :", astronaut[1])
        print("Agency :", astronaut[2])
        print("Missions :", astronaut[3])
        print("--------------------------------")


def assign_mission():

    aid = int(input("Enter Astronaut ID: "))

    for astronaut in astronauts:
        if astronaut[0] == aid:
            mission = input("Enter New Mission Name: ")
            astronaut[3].append(mission)
            print("Mission Assigned Successfully.")
            return

    print("Astronaut Not Found.")


def complete_mission():

    aid = int(input("Enter Astronaut ID: "))

    for astronaut in astronauts:
        if astronaut[0] == aid:

            mission = input("Enter Mission Name: ")

            if mission in astronaut[3]:
                astronaut[3].remove(mission)
                print("Mission Completed Successfully.")
            else:
                print("Mission Not Found.")

            return

    print("Astronaut Not Found.")


def search_astronaut():

    aid = int(input("Enter Astronaut ID: "))

    for astronaut in astronauts:

        if astronaut[0] == aid:

            print("\nAstronaut ID :", astronaut[0])
            print("Name :", astronaut[1])
            print("Agency :", astronaut[2])
            print("Missions :", astronaut[3])
            return

    print("Astronaut Not Found.")


def experienced_astronauts():

    print("\nExperienced Astronauts")

    for astronaut in astronauts:

        if len(astronaut[3]) >= 3:

            print("Name :", astronaut[1])
            print("Agency :", astronaut[2])
            print("Total Missions :", len(astronaut[3]))
            print("-------------------------")


def agency_count():

    agencies = []

    for astronaut in astronauts:
        if astronaut[2] not in agencies:
            agencies.append(astronaut[2])

    for agency in agencies:

        count = 0

        for astronaut in astronauts:
            if astronaut[2] == agency:
                count += 1

        print(agency, ":", count)


while True:

    print("\n===== Astronaut Mission Management System =====")
    print("1. Register New Astronaut")
    print("2. View All Astronauts")
    print("3. Assign New Mission")
    print("4. Complete Mission")
    print("5. Search Astronaut")
    print("6. Display Experienced Astronauts")
    print("7. Display Space Agency-wise Count")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        register_astronaut()

    elif choice == 2:
        view_astronauts()

    elif choice == 3:
        assign_mission()

    elif choice == 4:
        complete_mission()

    elif choice == 5:
        search_astronaut()

    elif choice == 6:
        experienced_astronauts()

    elif choice == 7:
        agency_count()

    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")