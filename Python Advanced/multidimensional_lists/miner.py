def read_matrix():
    matrix = []
    for row in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix


def start_position(matrix):
    start_coordinates = 0, 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 's':
                start_coordinates = [r, c]
    return start_coordinates


def read_command(matrix, command, row, column):
    if command == 'left':
        if column - 1 in range(len(matrix[0])):
            column -= 1
    elif command == 'right':
        if column + 1 in range(len(matrix[0])):
            column += 1
    elif command == 'up':
        if row - 1 in range(len(matrix)):
            row -= 1
    elif command == 'down':
        if row + 1 in range(len(matrix)):
            row += 1
    return [row, column]


def find_coals(matrix):
    found_coals = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'c':
                found_coals += 1
    return found_coals


def miner_moves(matrix, position):
    collected_coals = 0
    coals = 0
    [row, column] = position
    for command in commands:
        [row, column] = read_command(matrix, command, row, column)
        miner_move = matrix[row][column]
        if miner_move == 'e':
            return f"Game over! ({row}, {column})"
        elif miner_move == 'c':
            collected_coals += 1
            matrix[row][column] = '*'
            coals = find_coals(matrix)
            if coals == 0:
                return f"You collected all coals! ({row}, {column})"

    coals = find_coals(matrix)
    if coals == 0:
        return f"You collected all coals! ({row}, {column})"
    return f"{coals} coals left. ({row}, {column})"


rows = int(input())
commands = input().split()
matrix = read_matrix()
start = start_position(matrix)
print(miner_moves(matrix, start))

