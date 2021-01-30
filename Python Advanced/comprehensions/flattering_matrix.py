rows = int(input())
matrix = []
for _ in range(rows):
    row = input().split(', ')
    matrix.append(row)

flat = [int(x) for row in matrix for x in row]

print(flat)

