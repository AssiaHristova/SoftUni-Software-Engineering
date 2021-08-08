a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result_1 = a | b  # union
result_2 = a & b  # intersection
result_3 = a < b # subset true/false
result_4 = a - b # difference
result_5 = a ^ b # symmetric difference

result_1 = a.union(b)
result_2 = a.intersection(b)
result_3 = a.issubset(b)
result_4 = a.difference(b)
result_5 = a.symmetric_difference(b)
a.add(7)
a.remove(1)

# CTRL + / - закоментира/разкоментира много редове, първо трябва да ги маркираш с мишката
# ALT + click with the mouse - we can write the same thing on multiple lines

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(a)



