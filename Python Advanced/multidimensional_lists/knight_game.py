def read_matrix():
    rows = int(input())
    matrix = []
    for row in range(rows):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


def calculate_kills(matrix, row, column):
    kills = 0
    rows = [1, 1, 2, 2, -1, -1, -2, -2]
    columns = [2, -2, 1, -1, -2, 2, 1, -1]
    for index in range(len(rows)):
        if row + rows[index] in range(len(matrix)) and column + columns[index] in range(len(matrix)):
            potential_position = matrix[row + rows[index]][column + columns[index]]
            if potential_position == 'K':
                kills += 1
    return kills


def max_killer(matrix):
    max_kills = 0
    max_killer_coordinates = 0, 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'K':
                kills = calculate_kills(matrix, r, c)
                if kills > max_kills:
                    max_kills = kills
                    max_killer_coordinates = r, c
    if max_kills == 0:
        return None
    return max_killer_coordinates


def remove_max_killer(matrix, count):
    row, column = max_killer(matrix)
    matrix[row][column] = '0'
    count += 1
    return count


matrix = read_matrix()
count = 0
while max_killer(matrix) is not None:
    count = remove_max_killer(matrix, count)

print(count)


