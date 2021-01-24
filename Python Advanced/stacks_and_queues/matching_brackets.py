line = input()

s = []

for i in range(len(line)):
    char = line[i]
    if char == '(':
        s.append(i)
    elif char == ')':
        j = s.pop()
        print(line[j:i + 1])



