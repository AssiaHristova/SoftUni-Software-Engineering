string = input()
shuffles = int(input())

my_list = string.split(' ')
half = int(len(my_list) / 2)

for shuffle in range(shuffles):
    first_list = my_list[:half]
    second_list = my_list[half:]
    result_list = []
    index_first_list = 0
    for i in first_list:
        index_first_list += 1
        index_second_list = 0
        result_list.append(i)
        for j in second_list:
            index_second_list += 1
            if index_first_list == index_second_list:
               result_list.append(j)
    my_list = result_list
    if shuffle == shuffles - 1:
        print(result_list)

