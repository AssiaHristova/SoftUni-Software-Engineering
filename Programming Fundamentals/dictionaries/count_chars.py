string = input()

chars = {}

for char in string:
    if not ord(char) == 32:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

for char, count in chars.items():
    print(f'{char} -> {count}')