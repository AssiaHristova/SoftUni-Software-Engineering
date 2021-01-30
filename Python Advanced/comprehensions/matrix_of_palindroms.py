line = [int(x) for x in input().split()]

r, c = line
matrix = []
for _ in range(r):
    row = ['*'] * c
    matrix.append(row)

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix[r][c] = chr(97 + r) + chr(97 + r + c) + chr(97 + r)
        print(matrix[r][c], end=' ')
    print()




