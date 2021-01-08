command = input()

chat = []

while not command == "end":
    command_list = command.split()
    if 'Chat' in command_list:
        message = command_list[1]
        chat.append(message)
    elif 'Delete' in command_list:
        message = command_list[1]
        if message in chat:
            chat.remove(message)
    elif 'Edit' in command_list:
        message = command_list[1]
        edited_message = command_list[2]
        if message in chat:
            for i in range(len(chat)):
                if chat[i] == message:
                    chat[i] = edited_message
    elif 'Pin' in command_list:
        message = command_list[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif 'Spam' in command_list:
        command_list.remove('Spam')
        for element in command_list:
            chat.append(element)

    command = input()

print('\n'.join(chat))



