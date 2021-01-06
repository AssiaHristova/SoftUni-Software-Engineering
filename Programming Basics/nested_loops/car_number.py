start_num = int(input())
end_num = int(input())

flag_1 = True
flag_2 = True
flag_3 = True
flag_4 = True

for num_1 in range(start_num, end_num + 1):
    for num_2 in range(start_num, end_num + 1):
        for num_3 in range(start_num, end_num + 1):
            for num_4 in range(start_num, end_num + 1):
                if num_1 % 2 == 0 and num_4 % 2 != 0:
                    flag_1 = True
                else:
                    flag_1 = False
                if num_1 % 2 != 0 and num_4 % 2 == 0:
                    flag_2 = True
                else:
                    flag_2 = False
                if num_1 > num_4:
                    flag_3 = True
                else:
                    flag_3 = False
                if (num_2 + num_3) % 2 == 0:
                    flag_4 = True
                else:
                    flag_4 = False
                if (flag_1 or flag_2) and flag_3 and flag_4:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')




