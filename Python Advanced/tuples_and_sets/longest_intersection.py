import sys

n = int(input())

max_intersection = set()
max_length = -sys.maxsize

for _ in range(n):
    line = input().split('-')
    first_set = set()
    second_set = set()

    first_part = line[0].split(',')
    first_start = int(first_part[0])
    first_end = int(first_part[1])
    for num in range(first_start, first_end + 1):
        first_set.add(num)

    second_part = line[1].split(',')
    second_start = int(second_part[0])
    second_end = int(second_part[1])
    for num in range(second_start, second_end + 1):
        second_set.add(num)

    intersection = first_set.intersection(second_set)
    length = len(intersection)
    if length > max_length:
        max_length = length
        max_intersection = intersection

list_max_intersection = [el for el in max_intersection]

print(f"Longest intersection is {list_max_intersection} with length {max_length}")




