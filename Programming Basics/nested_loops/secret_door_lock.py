max_num_1 = int(input())
max_num_2 = int(input())
max_num_3 = int(input())

flag_1 = False
flag_2 = False
flag_3 = False

for num_1 in range(1, max_num_1 + 1):
    if num_1 % 2 == 0:
        flag_1 = True
    else:
        flag_1 = False
    for num_2 in range(2, max_num_2 + 1):
        for i in range(2, num_2):
            if num_2 % i == 0:
                flag_2 = False
                break
        else:
            flag_2 = True
        for num_3 in range(1, max_num_3 + 1):
            if num_3 % 2 == 0:
                flag_3 = True
            else:
                flag_3 = False
            if flag_1 and flag_2 and flag_3:
                print(f'{num_1} {num_2} {num_3}')
