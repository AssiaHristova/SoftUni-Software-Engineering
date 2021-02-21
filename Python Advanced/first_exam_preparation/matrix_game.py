def create_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


def find_start_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "P":
                return r, c


def invalid_move():
    return string[:-1]


def player_move(matrix, command, current_position):
    r, c = current_position
    if command == "up":
        if r - 1 in range(len(matrix)):
            return r - 1, c
        return invalid_move()
    elif command == "down":
        if r + 1 in range(len(matrix)):
            return r + 1, c
        return invalid_move()
    elif command == "left":
        if c - 1 in range(len(matrix[r])):
            return r, c - 1
        return invalid_move()
    elif command == "right":
        if c + 1 in range(len(matrix[r])):
            return r, c + 1
        return invalid_move()


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


string = input()
matrix = create_matrix()
current_position = find_start_position(matrix)
r, c = current_position
player_field = matrix[r][c]
m = int(input())

for _ in range(m):
    command = input()
    move = player_move(matrix, command, current_position)
    if move == string[:-1]:
        string = move
    else:
        matrix[r][c] = "-"
        r, c = move
        current_position = r, c
        current_field = matrix[r][c]
        if current_field.isalpha():
            string += current_field
            player_field = matrix[r][c] = "P"

print(string)
print_matrix(matrix)






