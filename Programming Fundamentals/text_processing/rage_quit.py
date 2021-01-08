text = input().upper()

text_list = []
unique = []
num_index = 0

for i in range(len(text)):
    if text[i].isdigit():
        if i + 1 in range(len(text)):
            if not text[i + 1].isdigit():
                text_list.append(text[num_index:(i + 1)])
                num_index = i + 1
            if text[i + 1].isdigit():
                text_list.append(text[num_index:(i + 2)])
                num_index = i + 2
        else:
            text_list.append(text[num_index:])
    else:
        if not text[i] in unique:
            unique.append(text[i])

print(f"Unique symbols used: {len(unique)}")

for ele in text_list:
    num = ''
    num_int = 0
    for symbol in ele:
        if symbol.isdigit():
            num += symbol
            num_int = int(num)
    new_ele = ele.replace(num, '')
    print(new_ele * num_int, end='')