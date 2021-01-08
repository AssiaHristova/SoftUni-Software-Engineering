list_1 = input().split(', ')
list_2 = input().split(', ')

result_list = []

for el in list_1:
    for word in list_2:
        if el in word:
            if el not in result_list:
                result_list.append(el)

print(result_list)