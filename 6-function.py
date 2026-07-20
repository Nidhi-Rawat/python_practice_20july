def circle(radius):
    pi = 3.14
    area = pi * radius * radius
    perimeter = 2 * pi * radius
    print("Area of the circle:", area)
    print("Perimeter of the circle:", perimeter)
radius = float(input("Enter the radius of the circle: "))
circle(radius)