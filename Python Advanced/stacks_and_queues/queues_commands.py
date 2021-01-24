from collections import deque

q = deque()
s = []
l = []

for i in range(1,6):
    q.append(i)
    s.append(i)
    l.append(i)

print('Queue:')
while q:
    print(q.popleft())

print('Stack:')
while s:
    print(s.pop())

print('List:')
while l:
    print(l.pop(0))
    




