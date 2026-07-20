players = []

n = int(input("Enter Number of Players: "))

for i in range(n):
    pid = int(input("Enter Player ID: "))
    name = input("Enter Player Name: ")
    team = input("Enter Team Name: ")
    matches = int(input("Enter Matches: "))
    runs = int(input("Enter Runs: "))
    centuries = int(input("Enter Centuries: "))
    half = int(input("Enter Half Centuries: "))

    stats = {
        "Matches": matches,
        "Runs": runs,
        "Centuries": centuries,
        "HalfCenturies": half
    }

    player = (pid, name, team, stats)

    players.append(player)
#register player
def register():
    pid = int(input("Enter Player ID: "))

    for p in players:
        if p[0] == pid:
            print("Player ID Already Exists")
            return

    name = input("Enter Name: ")
    team = input("Enter Team: ")
    matches = int(input("Enter Matches: "))
    runs = int(input("Enter Runs: "))
    centuries = int(input("Enter Centuries: "))
    half = int(input("Enter Half Centuries: "))

    stats = {
        "Matches": matches,
        "Runs": runs,
        "Centuries": centuries,
        "HalfCenturies": half
    }

    players.append((pid, name, team, stats))
    print("Player Registered Successfully")
#view players
def view():
    for p in players:
        print("\nID:", p[0])
        print("Name:", p[1])
        print("Team:", p[2])
        print("Statistics:", p[3])

def update():
    pid = int(input("Enter Player ID: "))

    for p in players:
        if p[0] == pid:

            field = input("Enter Field (Matches/Runs/Centuries/HalfCenturies): ")

            if field in p[3]:
                p[3][field] = int(input("Enter New Value: "))
                print("Updated Successfully")
            else:
                print("Invalid Field")
            return

    print("Player Not Found")

def search():
    pid = int(input("Enter Player ID: "))

    for p in players:
        if p[0] == pid:
            print(p)
            return

    print("Player Not Found")

def highest():
    top = players[0]

    for p in players:
        if p[3]["Runs"] > top[3]["Runs"]:
            top = p

    print("Highest Run Scorer")
    print(top)

def century():
    for p in players:
        if p[3]["Centuries"] > 10:
            print(p[1], p[3]["Centuries"])
def teamcount():
    teams = []

    for p in players:
        if p[2] not in teams:
            teams.append(p[2])

    for t in teams:
        count = 0

        for p in players:
            if p[2] == t:
                count += 1

        print(t, ":", count)
while True:

    print("\n1.Register")
    print("2.View")
    print("3.Update")
    print("4.Search")
    print("5.Highest Run Scorer")
    print("6.More Than 10 Centuries")
    print("7.Team-wise Count")
    print("8.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        register()
    elif ch == 2:
        view()
    elif ch == 3:
        update()
    elif ch == 4:
        search()
    elif ch == 5:
        highest()
    elif ch == 6:
        century()
    elif ch == 7:
        teamcount()
    elif ch == 8:
        break
    else:
        print("Invalid Choice")