customers = []

def add_customer():
    cid = int(input("Enter Customer ID: "))

    for c in customers:
        if c["CustomerId"] == cid:
            print("Customer ID Already Exists")
            return

    name = input("Enter Customer Name: ")
    city = input("Enter City: ")

    customers.append({
        "CustomerId": cid,
        "CustomerName": name,
        "City": city,
        "Orders": []
    })

    print("Customer Added")


def add_order():
    cid = int(input("Enter Customer ID: "))

    for c in customers:
        if c["CustomerId"] == cid:

            pid = int(input("Enter Product ID: "))
            pname = input("Enter Product Name: ")
            qty = int(input("Enter Quantity: "))
            price = int(input("Enter Price: "))

            c["Orders"].append({
                "ProductId": pid,
                "ProductName": pname,
                "Quantity": qty,
                "Price": price
            })

            print("Order Added")
            return

    print("Customer Not Found")


def view():
    for c in customers:
        print("\nCustomer ID:", c["CustomerId"])
        print("Name:", c["CustomerName"])
        print("City:", c["City"])

        for p in c["Orders"]:
            print(p)


def search():
    cid = int(input("Enter Customer ID: "))

    for c in customers:
        if c["CustomerId"] == cid:
            print(c)
            return

    print("Customer Not Found")


def update():
    cid = int(input("Enter Customer ID: "))
    pid = int(input("Enter Product ID: "))

    for c in customers:
        if c["CustomerId"] == cid:

            for p in c["Orders"]:
                if p["ProductId"] == pid:
                    p["Quantity"] = int(input("Enter New Quantity: "))
                    print("Quantity Updated")
                    return

    print("Record Not Found")


def remove():
    cid = int(input("Enter Customer ID: "))
    pid = int(input("Enter Product ID: "))

    for c in customers:
        if c["CustomerId"] == cid:

            for p in c["Orders"]:
                if p["ProductId"] == pid:
                    c["Orders"].remove(p)
                    print("Product Removed")
                    return

    print("Record Not Found")


def bill():
    cid = int(input("Enter Customer ID: "))

    for c in customers:
        if c["CustomerId"] == cid:

            total = 0

            for p in c["Orders"]:
                amount = p["Quantity"] * p["Price"]
                print(p["ProductName"], ":", amount)
                total += amount

            print("Total Bill:", total)
            return

    print("Customer Not Found")


def maximum():
    maxbill = 0
    customer = ""

    for c in customers:

        total = 0

        for p in c["Orders"]:
            total += p["Quantity"] * p["Price"]

        if total > maxbill:
            maxbill = total
            customer = c["CustomerName"]

    print("Customer:", customer)
    print("Total Amount:", maxbill)


while True:

    print("\n1.Add Customer")
    print("2.Add Product")
    print("3.View")
    print("4.Search")
    print("5.Update Quantity")
    print("6.Remove Product")
    print("7.Total Bill")
    print("8.Maximum Order Value")
    print("9.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add_customer()

    elif ch == 2:
        add_order()

    elif ch == 3:
        view()

    elif ch == 4:
        search()

    elif ch == 5:
        update()

    elif ch == 6:
        remove()

    elif ch == 7:
        bill()

    elif ch == 8:
        maximum()

    elif ch == 9:
        print("Thank You")
        break

    else:
        print("Invalid Choice")