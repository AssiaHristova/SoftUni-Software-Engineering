def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for row in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix


def find_square_matrix(matrix, size):
    coordinates = (0, 0)
    count = 0
    for r in range(len(matrix) - size + 1):
        for c in range(len(matrix[r]) - size + 1):
            if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
                coordinates = (r, c)
                count += 1
    return count


matrix = read_matrix()
size = 2
print(find_square_matrix(matrix, size))

