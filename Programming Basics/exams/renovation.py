import math

height = int(input())
width = int(input())
no_paint = int(input())
command = input()

paint = 0
painted_area = 0
area_left = 0

while command != "Tired!":
    area = (height * width) * 4
    area_to_paint = math.ceil(area * (1 - no_paint / 100))
    paint = int(command)
    painted_area += paint
    area_left = area_to_paint - painted_area
    if area_left <= 0:
        break

    command = input()

if command == "Tired!":
    print(f"{area_left} quadratic m left.")
else:
    if area_left == 0:
        print(f"All walls are painted! Great job, Pesho!")
    elif area_left <= 0:
        print(f"All walls are painted and you have {abs(area_left)} l paint left!")





