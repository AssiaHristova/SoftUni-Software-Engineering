rows = int(input())
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

command = input()

while not command == "END":
    data = command.split()
    command_word = data[0]
    row, col, value = [int(x) for x in data[1:]]
    if row in range(len(matrix)) and col in range(len(matrix)):
        if command_word == 'Add':
            matrix[row][col] += value
        elif command_word == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        print(matrix[row][col], end=' ')
    print()

