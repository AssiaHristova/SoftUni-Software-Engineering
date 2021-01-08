journal = input().split(', ')
command = input()

while not command == "Craft!":
    command_list = command.split(" - ")
    if 'Collect' in command_list:
        if command_list[1] not in journal:
            journal.append(command_list[1])
    elif "Drop" in command_list:
        if command_list[1] in journal:
            journal.remove(command_list[1])
    elif "Combine Items" in command_list:
        item_list = command_list[1].split(':')
        old_item = item_list[0]
        new_item = item_list[1]
        if old_item in journal:
            for i in range(len(journal)):
                if journal[i] == old_item:
                    journal.insert(i + 1, new_item)
    elif "Renew" in command_list:
        if command_list[-1] in journal:
            journal.remove(command_list[-1])
            journal.append(command_list[-1])

    command = input()

result = ', '.join(journal)
print(result)
