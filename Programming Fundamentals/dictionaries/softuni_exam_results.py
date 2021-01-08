data = input()

users = {}
languages = {}

while not data == "exam finished":
    data_list = data.split('-')
    if 'banned' in data_list:
        username = data_list[0]
        users[username] = 0
    else:
        username = data_list[0]
        language = data_list[1]
        points = int(data_list[2])
        if username in users:
            if points > users[username]:
                users[username] = points
        else:
            users[username] = points
        if language in languages:
            languages[language].append(username)
        else:
            languages[language] = [username]

    data = input()

sorted_users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
sorted_languages = dict(sorted(languages.items(), key=lambda x: (-len(x[1]), x[0])))

print('Results:')
for username, points in sorted_users.items():
    if points > 0:
        print(f'{username} | {points}')
print('Submissions:')
for language, username in sorted_languages.items():
    print(f'{language} - {len(username)}')




