import os

def create_file(file_name, content=''):
    with open(file_name, 'w') as file:
        file.write(content)


def add_content(file_name, content):
    with open(file_name, 'a') as file:
            file.write(content + '\n')


def replace_strings(file_name, old_string, new_string):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            modified_lines = [line.replace(old_string, new_string) for line in lines]
            content = ''.join(modified_lines)
            create_file(file_name, content)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


line = input()

while not line == "End":
    command = line.split('-')
    file_name = command[1]

    if command[0] == 'Create':
        create_file(file_name)

    elif command[0] == 'Add':
        content = command[2]
        add_content(file_name, content)

    elif command[0] == 'Replace':
        old_string, new_string = command[2:]
        replace_strings(file_name, old_string, new_string)

    elif command[0] == 'Delete':
        delete_file(file_name)

    line = input()