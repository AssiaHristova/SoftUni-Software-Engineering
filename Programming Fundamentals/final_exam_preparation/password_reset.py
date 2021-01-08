password = input()
word = input()

new_password = ''

while not word == "Done":
    command = word.split()
    if 'TakeOdd' in command:
        for i in range(1, len(password), 2):
            new_password += password[i]
        password = new_password
        print(password)
    elif 'Cut' in command:
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif 'Substitute' in command:
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    word = input()

print(f"Your password is: {password}")