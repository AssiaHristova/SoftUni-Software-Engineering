string = input().split(', ')

list_nums = [int(el) for el in string]
index = 10

while len(list_nums) > 0:
    group_of_index = [num for num in list_nums if num <= index]
    print(f"Group of {index}'s: {group_of_index}")
    list_nums = [el for el in list_nums if el not in group_of_index]
    group_of_index = []
    index += 10

