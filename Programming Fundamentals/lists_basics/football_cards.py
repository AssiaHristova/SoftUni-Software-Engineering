cards = input()

list_cards = cards.split(' ')
all_cards = set(list_cards)
team_A = 11
team_B = 11

for card in all_cards:
    if 'A' in card:
        team_A -= 1
    else:
        team_B -= 1
    if team_A < 7 or team_B < 7:
        break

print(f"Team A - {team_A}; Team B - {team_B}")
if team_A < 7 or team_B < 7:
    print("Game was terminated")
