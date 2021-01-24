n = int(input())

names = []

for _ in range(n):
    name = input()
    names.append(name)

unique_names = set(names)

for name in unique_names:
    print(name)





