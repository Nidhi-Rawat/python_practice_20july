patients = []

def add_patient():
    pid = int(input("Enter Patient ID: "))
    for p in patients:
        if p["PatientId"] == pid:
            print("Patient ID Already Exists")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")

    patients.append({
        "PatientId": pid,
        "PatientName": name,
        "Age": age,
        "City": city,
        "Visits": []
    })
    print("Patient Added")


def add_visit():
    pid = int(input("Enter Patient ID: "))

    for p in patients:
        if p["PatientId"] == pid:

            vid = int(input("Visit ID: "))

            for v in p["Visits"]:
                if v["VisitId"] == vid:
                    print("Visit ID Already Exists")
                    return

            doctor = input("Doctor Name: ")
            dept = input("Department: ")
            fee = int(input("Consultation Fee: "))
            med = int(input("Medicine Cost: "))
            status = input("Status: ")

            p["Visits"].append({
                "VisitId": vid,
                "DoctorName": doctor,
                "Department": dept,
                "ConsultationFee": fee,
                "MedicinesCost": med,
                "Status": status
            })

            print("Visit Added")
            return

    print("Patient Not Found")


def view():
    for p in patients:
        print("\nID:", p["PatientId"])
        print("Name:", p["PatientName"])
        print("Age:", p["Age"])
        print("City:", p["City"])

        for v in p["Visits"]:
            print(v)


def search():
    pid = int(input("Enter Patient ID: "))

    for p in patients:
        if p["PatientId"] == pid:
            print(p)
            print("Total Visits:", len(p["Visits"]))
            return

    print("Patient Not Found")


def update():
    pid = int(input("Enter Patient ID: "))
    vid = int(input("Enter Visit ID: "))

    for p in patients:
        if p["PatientId"] == pid:
            for v in p["Visits"]:
                if v["VisitId"] == vid:
                    v["Status"] = input("Enter New Status: ")
                    print("Status Updated")
                    return

    print("Record Not Found")


def bill():
    pid = int(input("Enter Patient ID: "))

    for p in patients:
        if p["PatientId"] == pid:

            total = 0

            for v in p["Visits"]:
                amount = v["ConsultationFee"] + v["MedicinesCost"]
                print("Visit Bill:", amount)
                total += amount

            print("Total Bill:", total)
            return

    print("Patient Not Found")


def multiple():
    for p in patients:
        if len(p["Visits"]) > 2:
            print(p["PatientId"], p["PatientName"], len(p["Visits"]))


def department():
    dept = []

    for p in patients:
        for v in p["Visits"]:
            if v["Department"] not in dept:
                dept.append(v["Department"])

    for d in dept:
        count = 0
        for p in patients:
            for v in p["Visits"]:
                if v["Department"] == d:
                    count += 1
        print(d, ":", count)


def highest():
    maxbill = 0
    patient = ""

    for p in patients:
        total = 0
        for v in p["Visits"]:
            total += v["ConsultationFee"] + v["MedicinesCost"]

        if total > maxbill:
            maxbill = total
            patient = p["PatientName"]

    print("Patient:", patient)
    print("Bill:", maxbill)


def remove():
    pid = int(input("Enter Patient ID: "))
    vid = int(input("Enter Visit ID: "))

    for p in patients:
        if p["PatientId"] == pid:
            for v in p["Visits"]:
                if v["VisitId"] == vid:
                    p["Visits"].remove(v)
                    print("Visit Removed")
                    return

    print("Record Not Found")


while True:

    print("\n1.Add Patient")
    print("2.Add Visit")
    print("3.View")
    print("4.Search")
    print("5.Update Status")
    print("6.Total Bill")
    print("7.Multiple Visits")
    print("8.Department Count")
    print("9.Highest Bill")
    print("10.Remove Visit")
    print("11.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add_patient()
    elif ch == 2:
        add_visit()
    elif ch == 3:
        view()
    elif ch == 4:
        search()
    elif ch == 5:
        update()
    elif ch == 6:
        bill()
    elif ch == 7:
        multiple()
    elif ch == 8:
        department()
    elif ch == 9:
        highest()
    elif ch == 10:
        remove()
    elif ch == 11:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
        