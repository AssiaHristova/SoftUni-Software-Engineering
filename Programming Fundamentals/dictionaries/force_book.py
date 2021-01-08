data = input()

users = {}

while not data == "Lumpawaroo":
    if '|' in data:
        data_list = data.split(' | ')
        user = data_list[1]
        side = data_list[0]
        if user not in users:
            users[user] = side
    elif '->' in data:
        data_list = data.split(' -> ')
        user = data_list[0]
        side = data_list[1]
        if user in users:
            users[user] = side
        else:
            users[user] = side
        print(f"{user} joins the {side} side!")

    data = input()

sides = {}

for user, side in users.items():
    if side not in sides:
        sides[side] = []
        sides[side].append(user)
    else:
        sides[side].append(user)
    sides[side] = sorted(sides[side])

sorted_sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))

for side, users in sorted_sides.items():
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
        print('! ', end='')
        print('\n! '.join(users))
