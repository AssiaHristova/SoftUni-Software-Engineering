factor = int(input())
count = int(input())

result = []
element = 0

while True:
    element += 1
    if element % factor == 0:
        result.append(element)
        if len(result) == count:
            break

print(result)


