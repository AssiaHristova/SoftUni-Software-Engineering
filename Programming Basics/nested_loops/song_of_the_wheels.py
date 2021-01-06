M = int(input())

count = 0
flag_1 = False
flag_2 = False
flag_3 = False
a_pass = 0
b_pass = 0
c_pass = 0
d_pass = 0


for a in range(1, 10):
    for b in range(1, 10):
        if a < b:
            flag_1 = True
        else:
            flag_1 = False
        for c in range(1, 10):
            for d in range(1, 10):
                if c > d:
                    flag_2 = True
                else:
                    flag_2 = False
                if (a * b) + (c * d) == M:
                    if flag_1 and flag_2:
                        count += 1
                        print(f'{a}{b}{c}{d}', end=' ')
                        if count == 4:
                            flag_3 = True
                            a_pass = a
                            b_pass = b
                            c_pass = c
                            d_pass = d

print()
if flag_3:
    print(f'Password: {a_pass}{b_pass}{c_pass}{d_pass}')
else:
    print('No!')

