for employee_id in range(1, 50):

    if employee_id == 37:
        break

    if employee_id % 5 == 0:
        continue

    if employee_id > 20:
        print(employee_id)