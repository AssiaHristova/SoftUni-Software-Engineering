def read_matrix():
    rows = int(input())
    matrix = []
    for row in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def sum_below_primary_diagonal(matrix):
    sum_below = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j:
                break
            sum_below += matrix[i][j]
    return sum_below


def sum_below_primary_diagonal_excluding(matrix):
    sum_below = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i <= j:
                break
            sum_below += matrix[i][j]
    return sum_below


def sum_below_primary_diagonal_2(matrix):
    sum_below = 0
    for i in range(len(matrix)):
        for j in range(i):  # for j in range(i + 1) - including the diagonal
            sum_below += matrix[i][j]
    return sum_below


def sum_above_primary_diagonal(matrix):
    sum_above = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):  # for j in range(i + 1, len(matrix) - including the diagonal
            sum_above += matrix[i][j]
    return sum_above


def sum_secondary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][len(matrix) - i -1]
    return diagonal_sum


print(primary_diagonal_sum(read_matrix()))
print(sum_below_primary_diagonal(read_matrix()))
print(sum_below_primary_diagonal_excluding(read_matrix()))
print(sum_above_primary_diagonal(read_matrix()))
print(sum_secondary_diagonal(read_matrix()))




