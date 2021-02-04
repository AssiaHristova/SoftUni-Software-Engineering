def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for row in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def best_coordinates(matrix, size):
    best_row_index = 0
    best_column_index = 0
    max_sum = sum_of_submatrix(matrix, best_row_index, best_column_index, size)
    for r in range(len(matrix) - size + 1):
        for c in range(len(matrix[r]) - size + 1):
            current_sum = sum_of_submatrix(matrix, r, c, size)
            if current_sum > max_sum:
                max_sum = current_sum
                best_row_index = r
                best_column_index = c
    return best_row_index, best_column_index


def print_result(matrix, coordinates, size):
    row_index, col_index = coordinates
    print(f'Sum = {sum_of_submatrix(matrix, row_index, col_index, size)}')
    for r in range(row_index, row_index + size):
        result = []
        for c in range(col_index, col_index + size):
            result.append(matrix[r][c])
        print(' '.join(str(x) for x in result))


matrix = read_matrix()
size = 3
print_result(matrix, best_coordinates(matrix, size), size)
