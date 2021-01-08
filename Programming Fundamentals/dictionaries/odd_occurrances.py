words = input().split()

words = [word.lower() for word in words]
occurrences = {}

for word in words:
    occurrences[word] = words.count(word)

for key, value in occurrences.items():
    if not value % 2 == 0:
        print(key, end=' ')
