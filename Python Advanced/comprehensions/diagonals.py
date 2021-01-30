rows = int(input())
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

first_diagonal = [matrix[i][i] for i in range(rows)]
second_diagonal = [matrix[i][rows - 1 - i] for i in range(rows)]

print(f"First diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")
