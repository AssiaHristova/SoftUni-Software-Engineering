text = input()

symbols = {}

for letter in text:
    count = text.count(letter)
    if letter not in symbols:
        symbols[letter] = count

sorted_symbols = sorted(symbols.items(), key=lambda x: x[0])

for element in sorted_symbols:
    print(f'{element[0]}: {element[1]} time/s')


