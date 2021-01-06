start_num = int(input())
end_num = int(input())

start_string = str(start_num)
end_string = str(end_num)
flag_a = False
flag_b = False
flag_c = False
flag_d = False

for a in range(int(start_string[0]), int(end_string[0]) + 1):
    for b in range(int(start_string[1]), int(end_string[1]) + 1):
        for c in range(int(start_string[2]), int(end_string[2]) + 1):
            for d in range(int(start_string[3]), int(end_string[3]) + 1):
                if a % 2 != 0:
                    flag_a = True
                else:
                    flag_a = False
                if b % 2 != 0:
                    flag_b = True
                else:
                    flag_b = False
                if c % 2 != 0:
                    flag_c = True
                else:
                    flag_c = False
                if d % 2 != 0:
                    flag_d = True
                else:
                    flag_d = False
                if flag_a and flag_b and flag_c and flag_d:
                    print(f'{a}{b}{c}{d}', end=' ')
