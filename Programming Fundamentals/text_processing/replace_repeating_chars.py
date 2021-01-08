text = input()

text_list = [char for char in text]

for i in range(len(text_list) - 1, -1, -1):
    if not i == 0:
        if text_list[i] == text_list[i - 1]:
            text_list.pop(i)

print(''.join(text_list))



