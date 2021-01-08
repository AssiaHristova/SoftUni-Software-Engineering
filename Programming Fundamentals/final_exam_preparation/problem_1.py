def case_lower(username):
    result = username.lower()
    print(result)
    return result


def case_upper(username):
    result = username.upper()
    print(result)
    return result


def reverse(username, start_i, end_i):
    if start_i in range(len(username)) and end_i in range(len(username)):
        substring = username[start_i:end_i + 1]
        result = substring[::-1]
        print(result)
        return username
    return username


def cut(username, substring):
    if substring in username:
        result = username.replace(substring, '', 1)
        print(result)
        return result
    print(f"The word {username} doesn't contain {substring}.")
    return username


def replace(username, char):
    if char in username:
        result = username.replace(char, '*')
        print(result)
        return result
    return username


def check(username, char):
    if char in username:
        print('Valid')
        return username
    print(f'Your username must contain {char}.')
    return username


username = input()
line = input()

while not line == 'Sign up':
    command = line.split()
    if command[0] == 'Case':
        if command[1] == 'lower':
            username = case_lower(username)
        elif command[1] == 'upper':
            username = case_upper(username)
    elif command[0] == 'Reverse':
        start_i = int(command[1])
        end_i = int(command[2])
        username = reverse(username, start_i, end_i)
    elif command[0] == 'Cut':
        substring = command[1]
        username = cut(username, substring)
    elif command[0] == 'Replace':
        char = command[1]
        username = replace(username, char)
    elif command[0] == 'Check':
        char = command[1]
        username = check(username, char)

    line = input()