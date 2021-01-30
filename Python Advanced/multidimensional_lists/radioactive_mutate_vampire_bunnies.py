def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for row in range(rows):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


def start_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                start_coordinates = [r, c]
                return start_coordinates


def bunnies_spread(matrix):
    bunnies = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                bunnies.append([r, c])
    for bunnie in bunnies:
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if [r, c] == bunnie:
                    if r + 1 in range(len(matrix)):
                        matrix[r + 1][c] = 'B'
                    if r - 1 in range(len(matrix)):
                        matrix[r - 1][c] = 'B'
                    if c + 1 in range(len(matrix[0])):
                        matrix[r][c + 1] = 'B'
                    if c + 1 in range(len(matrix[0])):
                        matrix[r][c - 1] = 'B'
                    break
    return matrix


def read_command(direction, row, column):
    if direction == 'L':
        column -= 1
    elif direction == 'R':
        column += 1
    elif direction == 'U':
        row -= 1
    elif direction == 'D':
        row += 1
    return [row, column]


def print_result(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end='')
        print()


def player_moves(matrix):
    row, column = start_position(matrix)
    matrix[row][column] = '.'
    for direction in directions:
        [row, column] = read_command(direction, row, column)
        if row in range(len(matrix)):
            if column in range(len(matrix[row])):
                player_move = matrix[row][column]
                matrix = bunnies_spread(matrix)
                if player_move == 'B':
                    print_result(matrix)
                    return f"dead: {row} {column}"
            else:
                print_result(matrix)
                return f"won: {row} {column}"
        else:
            print_result(matrix)
            return f"won: {row} {column}"
    print_result(matrix)
    return f"won: {row} {column}"


matrix = read_matrix()
directions = [el for el in input()]
print(player_moves(matrix))

