import math
employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students = int(input())

efficiency_per_hour = employee_1 + employee_2 + employee_3

hours = math.ceil(students / efficiency_per_hour)
for hour in range(1, hours + 1):
    if hour % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")


