shelf = input().split('&')
command = input()

while not command == "Done":
    command_list = command.split(' | ')
    first_command = command_list[0].split()
    if 'Add' in first_command:
        book_name = command_list[1]
        if book_name not in shelf:
            shelf.insert(0, book_name)
    elif 'Take' in first_command:
        book_name = command_list[1]
        if book_name in shelf:
            shelf.remove(book_name)
    elif 'Swap' in first_command:
        book_1 = command_list[1]
        book_2 = command_list[2]
        if book_1 in shelf and book_2 in shelf:
            index_1 = 0
            index_2 = 0
            for i in range(len(shelf)):
                if shelf[i] == book_1:
                    index_1 = i
            for j in range(len(shelf)):
                if shelf[j] == book_2:
                    index_2 = j
            shelf[index_1], shelf[index_2] = shelf[index_2], shelf[index_1]
    elif 'Insert' in first_command:
        book_name = command_list[1]
        shelf.append(book_name)
    elif 'Check' in first_command:
        index = int(command_list[1])
        if index in range(0, len(shelf)):
            print(shelf[index])

    command = input()

print(', '.join(shelf))
