def get_employee_details():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    overtime = int(input("Enter Overtime Hours: "))
    leave = int(input("Enter Leave Days: "))
    return emp_id, name, basic, overtime, leave


def calculate_hra(basic):
    return basic * 0.20


def calculate_da(basic):
    return basic * 0.10


def calculate_overtime(hours):
    return hours * 500


def calculate_leave_deduction(leave):
    if leave <= 2:
        return 0
    else:
        return (leave - 2) * 1000


def calculate_pf(basic):
    return basic * 0.12


def calculate_professional_tax(gross):
    if gross <= 30000:
        return 200
    elif gross <= 60000:
        return 500
    else:
        return 1000


def calculate_payroll(emp_id, name, basic, overtime, leave):

    hra = calculate_hra(basic)
    da = calculate_da(basic)
    overtime_pay = calculate_overtime(overtime)

    gross = basic + hra + da + overtime_pay

    pf = calculate_pf(basic)
    tax = calculate_professional_tax(gross)
    leave_deduction = calculate_leave_deduction(leave)

    total_deduction = pf + tax + leave_deduction

    net_salary = gross - total_deduction

    return hra, da, overtime_pay, gross, pf, tax, leave_deduction, total_deduction, net_salary


def display_salary_slip(emp_id, name, basic, hra, da, overtime_pay, gross, pf, tax, leave_deduction, total_deduction, net_salary):

    print("\n----------------------------------------")
    print("        EMPLOYEE SALARY SLIP")
    print("----------------------------------------")
    print("Employee ID       :", emp_id)
    print("Employee Name     :", name)
    print("Basic Salary      : ₹", basic)
    print("HRA               : ₹", hra)
    print("DA                : ₹", da)
    print("Overtime Payment  : ₹", overtime_pay)
    print("Gross Salary      : ₹", gross)
    print("PF Deduction      : ₹", pf)
    print("Professional Tax  : ₹", tax)
    print("Leave Deduction   : ₹", leave_deduction)
    print("Total Deduction   : ₹", total_deduction)
    print("Net Salary        : ₹", net_salary)
    print("----------------------------------------")


emp_id, name, basic, overtime, leave = get_employee_details()

hra, da, overtime_pay, gross, pf, tax, leave_deduction, total_deduction, net_salary = calculate_payroll(
    emp_id, name, basic, overtime, leave
)

display_salary_slip(
    emp_id, name, basic, hra, da, overtime_pay, gross,
    pf, tax, leave_deduction, total_deduction, net_salary
)

annual_salary = net_salary * 12

print("Annual Net Salary : ₹", annual_salary)