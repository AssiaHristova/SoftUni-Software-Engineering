def move(message, n):
    message = message[n:] + message[:n]
    return message


def insert(message, index, value):
    message = message[:index] + value + message[index:]
    return message


def change_all(message, substring, replacement):
    if substring in message:
        message = message.replace(substring, replacement)
    return message


message = input()
line = input()

while not line == "Decode":
    command = line.split('|')
    if 'Move' in command:
        n = int(command[1])
        message = move(message, n)
    elif 'Insert' in command:
        index = int(command[1])
        value = command[2]
        message = insert(message, index, value)
    elif 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)

    line = input()

print(f"The decrypted message is: {message}")
