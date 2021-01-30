line = input().split()

even_strings = [string for string in line if len(string) % 2 == 0]

for string in even_strings:
    print(string)

