import sys

player_name = input()

goals = 0
max_goals = -sys.maxsize
hat_trick = False
best_player = ''

while player_name != 'END':
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = player_name
    if goals >= 3:
        hat_trick = True
    if goals >= 10:
        break

    player_name = input()


print(f"{best_player} is the best player!")
if hat_trick:
    print(f"{best_player} has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} has scored {max_goals} goals.")