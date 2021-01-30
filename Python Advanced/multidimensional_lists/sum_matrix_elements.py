def read_matrix(is_test=False):
    if is_test:
        return [
            7, 1, 3, 3, 2, 1,
            7, 1, 3, 3, 2, 1,
            7, 1, 3, 3, 2, 1,
        ]
    rows, columns = map(int, input().split(', '))
    matrix = []  # matrix = [list(map(int, input().split(', '))) for _ in range(rows)] DON'T DO THIS
    for row in range(rows):
        row = list(map(int, input().split(', ')))  # row = [int(r) for r  in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        matrix_sum += row[c]

print(matrix_sum)
print(matrix)





