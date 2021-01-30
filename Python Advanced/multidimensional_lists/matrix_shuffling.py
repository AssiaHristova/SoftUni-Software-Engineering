def read_matrix():
    rows, columns = map(int, input().split())
    matrix = []
    for row in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix, rows, columns


def swap_command(matrix, coordinates_list):
    [row1, col1, row2, col2] = coordinates_list
    first_point = matrix[row1][col1]
    second_point = matrix[row2][col2]
    if not first_point == second_point:
        matrix[row1][col1] = second_point
        matrix[row2][col2] = first_point
    return matrix


def is_valid(rows, columns, command_list, coordinates_list):
    is_valid = False
    if command_list[0] == 'swap' and len(coordinates_list) == 4:
        if coordinates_list[0] in range(rows) and coordinates_list[2] in range(rows):
            if coordinates_list[1] in range(columns) and coordinates_list[3] in range(columns):
                is_valid = True
    return is_valid


def print_result(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end=' ')
        print()


matrix, rows, columns = read_matrix()
command = input()

while not command == 'END':
    command_list = command.split()
    coordinates_list = command_list[1:]
    coordinates_list = [int(x) for x in coordinates_list]
    if is_valid(rows, columns, command_list, coordinates_list):
        matrix = swap_command(matrix, coordinates_list)
        print_result(matrix)
    else:
        print("Invalid input!")

    command = input()



