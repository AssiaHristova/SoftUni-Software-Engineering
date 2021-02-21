def create_board():
    board = []
    for _ in range(8):
        line = input().split()
        board.append(line)
    return board


def find_the_king(board):
    for r in range(len(board)):
        if 'K' in board[r]:
            c = board[r].index('K')
            return r, c


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    col_count = len(board[0])
    r, c = king
    delta_row, delta_col = deltas
    while in_range(r, rows_count) and in_range(c, col_count):
        if board[r][c] == 'Q':
            return r, c
        r += delta_row
        c += delta_col


def find_the_killer_queens(king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, + 1),
        (0, + 1),
        (+ 1, + 1),
        (+ 1, 0),
        (+1, -1)
    ]
    queens = [search_with_deltas(board, king, delta) for delta in deltas]
    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print([*queen])
    else:
        print('The king is safe!')


board = create_board()
king = find_the_king(board)
queens = find_the_killer_queens(king)
print_result(queens)
