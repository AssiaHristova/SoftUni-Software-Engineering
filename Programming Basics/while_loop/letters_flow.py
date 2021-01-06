symbol = input()

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'f', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'F', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
count_n = 0
count_c = 0
count_o = 0
word = ''

while symbol != 'End':
    letter = symbol
    if letter in small_letters or letter in capital_letters:
        if letter == 'c':
            count_c += 1
            if count_c != 1:
                word += letter
        elif letter == 'o':
            count_o += 1
            if count_o != 1:
                word += letter
        elif letter == 'n':
            count_n += 1
            if count_n != 1:
                word += letter
        else:
            word += letter
    if count_c >= 1 and count_n >= 1 and count_c >= 1:
        print(word, end=' ')
        count_n = 0
        count_c = 0
        count_o = 0
        word = ''

    symbol = input()