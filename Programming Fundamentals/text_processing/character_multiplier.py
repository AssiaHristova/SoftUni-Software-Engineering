data = input().split()

result = 0
string_1 = data[0]
string_2 = data[1]

if len(string_2) > len(string_1):
    for i in range(len(string_1)):
        result += ord(string_1[i]) * ord(string_2[i])
    for j in range(len(string_2)):
        if j >= len(string_1):
            result += ord(string_2[j])
else:
    for j in range(len(string_2)):
        result += ord(string_1[j]) * ord(string_2[j])
    for i in range(len(string_1)):
        if i >= len(string_2):
            result += ord(string_1[i])

print(result)
