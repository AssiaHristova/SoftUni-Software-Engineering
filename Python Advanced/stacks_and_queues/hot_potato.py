from collections import deque

line = input().split()
n = int(input())

kids = deque()

for el in line:
    kids.append(el)

counter = 1
while len(kids) > 1:
    if counter == n:
        counter = 1
        print(f'Removed {kids.popleft()}')
    else:
        kid = kids.popleft()
        kids.append(kid)
        counter += 1

print(f'Last is {kids.popleft()}')
