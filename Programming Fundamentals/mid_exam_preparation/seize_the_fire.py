fire_level = input().split('#')
water = int(input())

effort = 0
total_fire = 0
cells = []

for element in fire_level:
    cell = element.split(' = ')
    level = cell[0]
    fire = int(cell[1])
    if level == 'High':
        if fire in range(81, 126):
            if water - fire >= 0:
                water -= fire
                effort += fire * 0.25
                total_fire += fire
                cells.append(fire)
    elif level == 'Medium':
        if fire in range(51, 81):
            if water - fire >= 0:
                water -= fire
                effort += fire * 0.25
                total_fire += fire
                cells.append(fire)
    elif level == 'Low':
        if fire in range(1, 51):
            if water - fire >= 0:
                water -= fire
                effort += fire * 0.25
                total_fire += fire
                cells.append(fire)

cells_str = [str(cell) for cell in cells]

print("Cells:")
print(' - ', end='')
print('\n - '.join(cells_str))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")