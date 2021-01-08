def contains(activation_key, substring):
    if substring in activation_key:
        print(f"{activation_key} contains {substring}")
    else:
        print(f"Substring not found!")
    return activation_key


def flip(activation_key, action, start_i, end_i):
    substring = activation_key[start_i:end_i]
    if action == 'Upper':
        substring = substring.upper()
    elif action == 'Lower':
        substring = substring.lower()
    result = activation_key[:start_i] + substring + activation_key[end_i:]
    print(result)
    return result


def slice(activation_key, start_i, end_i):
    activation_key = activation_key[:start_i] + activation_key[end_i:]
    print(activation_key)
    return activation_key


activation_key = input()
instructions = input()

while not instructions == "Generate":
    command = instructions.split(">>>")
    if command[0] == 'Contains':
        substring = command[1]
        activation_key = contains(activation_key, substring)
    elif command[0] == 'Flip':
        action = command[1]
        start_i = int(command[2])
        end_i = int(command[3])
        activation_key = flip(activation_key, action, start_i, end_i)
    elif command[0] == 'Slice':
        start_i = int(command[1])
        end_i = int(command[2])
        activation_key = slice(activation_key, start_i, end_i)

    instructions = input()

print(f"Your activation key is: {activation_key}")