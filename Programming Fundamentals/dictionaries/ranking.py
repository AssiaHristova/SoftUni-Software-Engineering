import sys

line = input()

contests = {}
users = {}
contests_per_user = {}
max_points = -sys.maxsize
max_user = ''

while not line == "end of contests":
    line_list = line.split(':')
    contest = line_list[0]
    password = line_list[1]
    contests[contest] = password

    line = input()

data = input()

while not data == "end of submissions":
    data_list = data.split('=>')
    contest = data_list[0]
    password = data_list[1]
    username = data_list[2]
    points = int(data_list[3])
    if contest in contests:
        if password == contests[contest]:
            if username in users:
                if users[username][0] == contest:
                    if points > users[username][1]:
                        users[username][1] = points
                else:
                    users[username] += [contest, points]
            else:
                users[username] = contests_per_user
                contests_per_user[contest] = points

    data = input()

for user, value in users.items():
    total_points = 0
    for i in range(1, len(value), 2):
        total_points += value[i]
        if total_points > max_points:
            max_points = total_points
            max_user = user

print(f"Best candidate is {max_user} with total {max_points} points.")

users_sorted = sorted(users.items(), key=lambda x: (x[0], -x[1][1]))
print(users_sorted)

for user in users_sorted:
    print('Ranking:')
    print(f'{user[0]}')
    print(f'#  {user[1][0]} -> {user[1][1]}')