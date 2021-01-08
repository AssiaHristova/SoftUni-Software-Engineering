def insert_space(message, index):
    result = ''
    result = message[:index] + ' ' + message[index:]
    print(result)
    return result


def reverse(message, substring):
    result = ''
    if substring in message:
        result = message.replace(substring, '', 1)
        result += substring[::-1]
        print(result)
    else:
        result = message
        print("error")
    return result


def change_all(message, substring, replacement):
    result = ''
    if substring in message:
        result = message.replace(substring, replacement)
    print(result)
    return result


message = input()
line = input()

while not line == "Reveal":
    command = line.split(":|:")
    if command[0] == 'InsertSpace':
        index = int(command[1])
        message = insert_space(message, index)
    elif command[0] == 'Reverse':
        substring = command[1]
        message = reverse(message, substring)
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)

    line = input()

print(f"You have a new text message: {message}")
