words = input().split()
command = input()

while not command == "Stop":
    command_list = command.split()
    if 'Delete' == command_list[0]:
        index = int(command_list[1])
        if index in range(0, len(words)):
            words.pop(index + 1)
    elif 'Swap' == command_list[0]:
        word_1 = command_list[1]
        word_2 = command_list[2]
        index_1 = 0
        index_2 = 0
        if word_1 in words and word_2 in words:
            for i in range(0, len(words)):
                if words[i] == word_1:
                    index_1 = i
            for j in range(0, len(words)):
                if words[j] == word_2:
                    index_2 = j
            words[index_1], words[index_2] = words[index_2], words[index_1]
    elif 'Put' == command_list[0]:
        word = command_list[1]
        index = int(command_list[2])
        if index in range(0, len(words)):
            words.insert(index - 1, word)
    elif 'Sort' == command_list[0]:
        words.sort(reverse=True)
    elif 'Replace' == command_list[0]:
        word_1 = command_list[1]
        word_2 = command_list[2]
        if word_2 in words:
            for i in range(0, len(words)):
                if words[i] == word_2:
                    words[i] = word_1

    command = input()

print(' '.join(words))



