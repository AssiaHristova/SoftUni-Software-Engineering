n = int(input())
word = input()

result = []
key_word = []

for i in range(n):
    string = input()
    result.append(string)
    if word in string:
        key_word.append(string)

print(result)
print(key_word)


