start_num_first_pair = int(input())
start_num_second_pair = int(input())
result_first_pair = int(input())
result_second_pair = int(input())

flag_1 = False
flag_2 = False

for ab in range(start_num_first_pair, (result_first_pair + start_num_first_pair) + 1):
    for i in range(2, ab):
        if ab % i == 0:
            flag_1 = False
            break
    else:
        flag_1 = True
    for cd in range(start_num_second_pair, (result_second_pair + start_num_second_pair) + 1):
        for j in range(2, cd):
            if cd % j == 0:
                flag_2 = False
                break
        else:
            flag_2 = True
        if flag_1 and flag_2:
            print(f'{ab}{cd}')



