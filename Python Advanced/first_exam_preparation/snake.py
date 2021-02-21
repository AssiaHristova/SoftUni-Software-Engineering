def create_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


def find_the_snake(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'S':
                return r, c


def snake_move(command, snake_position):
    r, c = snake_position
    if command == 'up':
        r -= 1
    elif command == 'down':
        r += 1
    elif command == 'left':
        c -= 1
    elif command == 'right':
        c += 1
    return r, c


def is_move_valid(snake_move):
    r, c = snake_move
    if r in range(len(matrix)) and c in range(len(matrix)):
        return True
    return False


def snake_trail(matrix, snake_position):
    r, c = snake_position
    matrix[r][c] = '.'
    return matrix


def has_food(current_position):
    r, c = current_position
    if matrix[r][c] == '*':
        return True
    return False


def has_burrow(current_position):
    r, c = current_position
    if matrix[r][c] == 'B':
        return True
    return False


def find_second_barrow(matrix, current_position):
    r, c = current_position
    if matrix[r][c] == 'B':
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 'B' and (row != r or col != c):
                    return row, col


def locate_the_snake(matrix, snake_position):
    r, c = snake_position
    matrix[r][c] = 'S'
    return matrix


def print_result(matrix):
    for row in matrix:
        print(''.join(row))


matrix = create_matrix()
snake_position = find_the_snake(matrix)
food = 0
while True:
    command = input()
    if command == '':
        matrix = locate_the_snake(matrix, snake_position)
        break
    matrix = snake_trail(matrix, snake_position)
    move = snake_move(command, snake_position)
    if not is_move_valid(move):
        print("Game over!")
        break
    else:
        current_position = move
        if has_food(current_position):
            food += 1
            snake_position = current_position
            if food == 10:
                matrix = locate_the_snake(matrix, snake_position)
                print("You won! You fed the snake.")
                break
        elif has_burrow(current_position):
            new_position = find_second_barrow(matrix, current_position)
            matrix = snake_trail(matrix, current_position)
            snake_position = new_position
        else:
            snake_position = current_position


print(f"Food eaten: {food}")
print_result(matrix)






