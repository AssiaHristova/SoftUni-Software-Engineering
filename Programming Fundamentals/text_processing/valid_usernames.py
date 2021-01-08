usernames = input().split(', ')

for username in usernames:
    is_valid = False
    if len(username) in range(3, 17):
        if username.isalnum():
            is_valid = True
        else:
            for symbol in username:
                if symbol == '-' or symbol == '_':
                    is_valid = True
    if is_valid:
        print(username.strip())
