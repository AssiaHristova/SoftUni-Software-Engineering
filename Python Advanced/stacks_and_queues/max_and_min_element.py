N = int(input())

sequence = []

PUSH = '1'
DELETE = '2'
MAX = '3'
MIN = '4'

for i in range(N):
    query = input().split()
    if query[0] == PUSH:
        sequence.append(int(query[1]))
    elif query[0] == DELETE:
        if sequence:
            sequence.pop()
    elif query[0] == MAX:
        print(max(sequence))
    elif query[0] == MIN:
        print(min(sequence))

while sequence:
    if len(sequence) == 1:
        print(sequence. pop(), end=' ')
    else:
        print(sequence.pop(), end=', ')


