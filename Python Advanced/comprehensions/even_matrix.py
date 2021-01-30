rows = int(input())
matrix = []
for _ in range(rows):
    row = input().split(', ')
    matrix.append(row)

even_matrix = [[int(x) for x in row if int(x) % 2 == 0] for row in matrix]


def get_even(values):
    return [int(x) for x in values if int(x) % 2 == 0]


even_matrix_2 = [get_even(row) for row in matrix]

print(even_matrix)
print(even_matrix_2)