string = input().split()

result = 0
total_sum = 0

for word in string:
    word.strip()
    letter_before = word[0]
    letter_after = word[-1]
    num = int(word[1: -1])
    if letter_before.isupper():
        result = num / (ord(letter_before) - 64)
    else:
        result = num * (ord(letter_before) - 96)
    if letter_after.isupper():
        result -= (ord(letter_after) - 64)
    else:
        result += (ord(letter_after) - 96)

    total_sum += result

print(f'{total_sum:.2f}')
