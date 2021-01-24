from collections import deque

line = input().split()
n = int(input())

kids = deque()

for el in line:
    kids.append(el)

while len(kids) > 1:
    for _ in range(n - 1):
        kids.append(kids.popleft())
    print(f'Removed {kids.popleft()}')

print(f'Last is {kids.popleft()}')
