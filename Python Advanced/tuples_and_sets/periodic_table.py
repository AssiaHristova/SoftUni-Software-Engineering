n = int(input())

unique_elements = set()

for _ in range(n):
    line = input().split()
    for el in line:
        if el not in unique_elements:
            unique_elements.add(el)

for el in unique_elements:
    print(el)

