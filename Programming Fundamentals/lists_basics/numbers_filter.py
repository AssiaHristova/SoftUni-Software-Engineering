n = int(input())

positive = []
negative = []
even = []
odd = []

for i in range(n):
    integer = int(input())
    if integer >= 0:
        positive.append(integer)
    if integer < 0:
        negative.append(integer)
    if integer % 2 == 0:
        even.append(integer)
    if not integer % 2 == 0:
        odd.append(integer)

command = input()
if command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)
elif command == 'even':
    print(even)
else:
    print(odd)




