message = input().split()

for word in message:
    deciphered_message = []
    ascii_list = []
    words_list = []
    for letter in word:
        if letter.isdigit():
            ascii_list.append(letter)
        else:
            words_list.append(letter)

    words_list[0], words_list[-1] = words_list[-1], words_list[0]
    ascii_letter = ''.join(ascii_list)
    ascii_symbol = chr(int(ascii_letter))
    words_list.insert(0, ascii_symbol)
    deciphered_message = ''.join(words_list)
    print(deciphered_message, end=' ')




