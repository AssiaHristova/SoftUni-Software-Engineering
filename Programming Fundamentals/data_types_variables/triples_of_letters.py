n = int(input())

for i in range(n):
    letter_1 = chr(97 + i)
    for j in range(n):
        letter_2 = chr(97 + j)
        for k in range(n):
            letter_3 = chr(97 + k)
            print(f'{letter_1}{letter_2}{letter_3}')







