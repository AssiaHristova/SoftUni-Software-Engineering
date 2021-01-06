trunk_capacity = float(input())
command = input()

suitcases = 0
free_space = trunk_capacity

while command != 'End':
    suitcase_capacity = float(command)
    free_space -= suitcase_capacity
    if free_space <= 0:
        break
    suitcases += 1
    if suitcases % 3 == 0:
        suitcase_capacity = suitcase_capacity * 1.10

    command = input()

if free_space > 0:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {suitcases} suitcases loaded.")



