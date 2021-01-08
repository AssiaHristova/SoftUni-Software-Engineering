char = input()
char_2 = input()
text = input()

result = 0

for el in text:
    if ord(el) in range(ord(char) + 1, ord(char_2)):
        result += ord(el)

print(result)