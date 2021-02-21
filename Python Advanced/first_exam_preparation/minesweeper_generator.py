def create_field(n):
    field = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append('')
        field.append(row)
    return field


def placing_bombs(field, bombs):
    for _ in range(bombs):
        line = input()[1:-1]
        bomb_position = [int(el) for el in line.split(', ')]
        r, c = bomb_position
        field[r][c] = '*'
    return field


def calculating_numbers(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if not field[r][c] == '*':
                number = 0
                if r + 1 in range(len(field)):
                    if field[r + 1][c] == '*':
                        number += 1
                if r + 1 in range(len(field)) and c + 1 in range(len(field)):
                    if field[r + 1][c + 1] == '*':
                        number += 1
                if r + 1 in range(len(field)) and c - 1 in range(len(field)):
                    if field[r + 1][c - 1] == '*':
                        number += 1
                if r - 1 in range(len(field)):
                    if field[r - 1][c] == '*':
                        number += 1
                if r - 1 in range(len(field)) and c + 1 in range(len(field)):
                    if field[r - 1][c + 1] == '*':
                        number += 1
                if r - 1 in range(len(field)) and c - 1 in range(len(field)):
                    if field[r - 1][c - 1] == '*':
                        number += 1
                if c + 1 in range(len(field)):
                    if field[r][c + 1] == '*':
                        number += 1
                if c - 1 in range(len(field)):
                    if field[r][c - 1] == '*':
                        number += 1
                field[r][c] = number
    return field


def print_result(field):
    for row in field:
        print(*row)


n = int(input())
bombs = int(input())
empty_field = create_field(n)
field_with_bombs = placing_bombs(empty_field, bombs)
result_field = calculating_numbers(field_with_bombs)
print_result(result_field)

