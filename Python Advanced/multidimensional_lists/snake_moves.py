from collections import deque


def create_snake(snake):
    snake_queue = deque()
    for el in snake:
        snake_queue.append(el)
    return snake_queue


def create_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = [0] * columns
        matrix.append(row)
    return matrix


def snake_moves(matrix, rows, columns, snake_queue):
    for r in range(rows):
        if not r % 2 == 0:
            for c in range(-1, -columns - 1, -1):
                x = snake_queue.popleft()
                matrix[r][c] = x
                snake_queue.append(x)
        else:
            for c in range(columns):
                x = snake_queue.popleft()
                matrix[r][c] = x
                snake_queue.append(x)
    return matrix


def print_result(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end='')
        print()


line = input().split()
snake = input()

rows = int(line[0])
columns = int(line[1])

snake_queue = create_snake(snake)
matrix = create_matrix(rows, columns)
matrix = snake_moves(matrix, rows, columns, snake_queue)
print_result(matrix)


