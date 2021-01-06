N = int(input())

flag_1 = True
flag_2 = True

for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                if (num_1 + num_2) == (num_3 + num_4):
                    flag_1 = True
                else:
                    flag_1 = False
                if N % (num_1 + num_2) == 0:
                    flag_2 = True
                else:
                    flag_2 = False
                if flag_1 and flag_2:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')


