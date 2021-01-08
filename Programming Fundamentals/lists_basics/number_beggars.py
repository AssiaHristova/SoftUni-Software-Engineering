string = input()
beggars = int(input())

string_list = string.split(',')
num_list = []
result = []
index = 0

for element in string_list:
    num_element = int(element)
    num_list.append(num_element)

for beggar in range(beggars):
    result_1 = num_list[index:(len(num_list) + 1):beggars]
    result.append(sum(result_1))
    index += 1

print(result)






