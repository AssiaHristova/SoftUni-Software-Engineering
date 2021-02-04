matrix = []

rows = 3
columns = 2

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(0)
    matrix.append(row)

print(matrix)

matrix = [[0] * columns for _ in range(rows)]

print(matrix)

matrix = []

for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        matrix[i].append(j)

print(matrix)