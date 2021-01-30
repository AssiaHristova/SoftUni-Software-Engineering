line = [x for x in input().split('|')]

values = [int(x) for string in line[::-1] for x in string.split()]

print(*values)


