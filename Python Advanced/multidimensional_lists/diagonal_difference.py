def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def sum_secondary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][len(matrix) - i - 1]
    return diagonal_sum


matrix = read_matrix()
result = abs(primary_diagonal_sum(matrix) - sum_secondary_diagonal(matrix))
print(result)
