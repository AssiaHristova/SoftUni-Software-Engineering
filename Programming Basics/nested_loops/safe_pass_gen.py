a = int(input())
b = int(input())
max_pass = int(input())

count_pass = 0

for x in range(1, a + 1):
    if x > 1:
        A += 1
        B += 1
    for y in range(1, b + 1):
                if y > 1:
                    A += 1
                    B += 1
                    for A in range(35, 56):
                        if A > 55:
                            A -= 20
                        for B in range(64, 97):
                            if B > 96:
                                B -= 32
                count_pass += 1
                if count_pass > max_pass:
                    break
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')