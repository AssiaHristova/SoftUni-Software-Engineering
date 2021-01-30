def read_matrix():
    rows, columns = map(int, input().split(', '))
    matrix = []
    for row in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def column_sum(matrix):
    sums = []
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for i in range(columns_count):
        column_sum = 0
        for j in range(rows_count):
            column_sum += matrix[j][i]
        sums.append(column_sum)
    return sums


def print_result(values):
    [print(x) for x in values]


matrix = read_matrix()
result = column_sum(matrix)
print_result(result)