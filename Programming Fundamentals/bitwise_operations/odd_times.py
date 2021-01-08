line = input().split()

num_list = [int(num) for num in line]

for i in range(len(num_list) - 1):
    count = 0
    if num_list[i] ^ 0 in num_list[i + 1:]:
        count = num_list.count(num_list[i])
    if not count % 2 == 0:
        print(num_list[i])
        break




