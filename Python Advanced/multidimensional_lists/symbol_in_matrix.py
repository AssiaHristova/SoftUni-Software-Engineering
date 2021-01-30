def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        row = [ord(x) for x in input()]
        matrix.append(row)
    return matrix


def symbol_in_matrix(matrix, symbol):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_symbol = matrix[i][j]
            if ord(symbol) == current_symbol:
                return f"({i}, {j})"
    return f"{symbol} does not occur in the matrix"


matrix = read_matrix()
symbol = input()
print(symbol_in_matrix(matrix, symbol))



