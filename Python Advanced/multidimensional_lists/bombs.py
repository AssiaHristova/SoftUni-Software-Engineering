def read_matrix():
    rows = int(input())
    matrix = []
    for row in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def create_bombs(indexes):
    bombs = []
    for index in indexes:
        coordinate = index.split(',')
        row = int(coordinate[0])
        column = int(coordinate[1])
        bombs.append([row, column])
    return bombs


def damaged_matrix(matrix, row_index, column_index, bomb_value):
    for r in range(row_index - 1, row_index + 2):
        if r in range(len(matrix)):
            for c in range(column_index - 1, column_index + 2):
                if c in range(len(matrix[r])):
                    if matrix[r][c] > 0:
                        matrix[r][c] -= bomb_value
    return matrix


def exploded_bombs(matrix, bombs):
    bomb_values = []
    for bomb in bombs:
        row, column = bomb
        bomb_value = matrix[row][column]
        bomb_values.append(bomb_value)
    for i in range(len(bombs)):
        row, column = bombs[i]
        bomb_value = bomb_values[i]
        matrix = damaged_matrix(matrix, row, column, bomb_value)
        matrix[row][column] = 0
    return matrix


def alive_cells(matrix):
    alive_cells = 0
    sum_alive_cells = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 0:
                alive_cells += 1
                sum_alive_cells += matrix[r][c]
    return [alive_cells, sum_alive_cells]


def print_result(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')
        print()


matrix = read_matrix()
indexes = input().split()
bombs = create_bombs(indexes)
matrix = exploded_bombs(matrix, bombs)
print(f"Alive cells: {alive_cells(matrix)[0]}")
print(f"Sum: {alive_cells(matrix)[1]}")
print_result(matrix)







