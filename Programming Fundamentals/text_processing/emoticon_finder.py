text = input()

for i in range(len(text)):
    if text[i] == ':':
        print(text[i], end='')
        print(text[i + 1])




