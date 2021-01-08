fires_and_cells = input()
water = int(input())

list_fires_and_cells = fires_and_cells.split('#')
water_left = water
list_of_cells = []
effort = 0
total_fire = 0

for element in list_fires_and_cells:
    list_of_elements = element.split(' ')
    cell = int(list_of_elements[-1])
    if list_of_elements[0] == 'High':
        if 81 <= cell <= 125:
            if water_left - cell >= 0:
                water_left -= cell
                effort += cell / 4
                total_fire += cell
                list_of_cells.append(cell)
    elif list_of_elements[0] == 'Medium':
        if 51 <= cell <= 80:
            if water_left - cell >= 0:
                water_left -= cell
                effort += cell / 4
                total_fire += cell
                list_of_cells.append(cell)
    elif list_of_elements[0] == 'Low':
        if 1 <= cell <= 50:
            if water_left - cell >= 0:
                water_left -= cell
                effort += cell / 4
                total_fire += cell
                list_of_cells.append(cell)

print("Cells:")
for cell in list_of_cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




