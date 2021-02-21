import math


def create_matrix(n):
    matrix = []
    for _ in range(n):
        line = input().split()
        matrix.append(line)
    return matrix


def find_the_player(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                return r, c


def player_move(player_position, command):
    r, c = player_position
    if command == 'up':
        r -= 1
    elif command == 'down':
        r += 1
    elif command == 'left':
        c -= 1
    elif command == 'right':
        c += 1
    return r, c


def is_move_valid(player_move):
    r, c = player_move
    if r in range(len(matrix)) and c in range(len(matrix)):
        if not matrix[r][c] == 'X':
            return True
    return False


n = int(input())
matrix = create_matrix(n)
player_position = find_the_player(matrix)
coins = 0
player_path = []
win = False

while True:
    command = input()
    if command == '':
        break
    move = player_move(player_position, command)
    if not is_move_valid(move):
        coins = math.floor(coins * 0.5)
        break
    else:
        r, c = move
        player_path.append([r, c])
        player_field = matrix[r][c]
        coins += int(player_field)
        player_position = move
    if coins >= 100:
        win = True
        break

if win:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path: ")
for el in player_path:
    print(f"{el}")
