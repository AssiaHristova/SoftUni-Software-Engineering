char_1 = input()
char_2 = input()


def chars_between(symbol_1, symbol_2):
    symbols = []
    for symbol in range(ord(symbol_1) + 1, ord(symbol_2)):
       symbols.append(chr(symbol))
    string = ' '.join(symbols)
    return string


print(chars_between(char_1, char_2))

