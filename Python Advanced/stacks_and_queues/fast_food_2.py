from collections import deque

food = int(input())
line = input().split()

orders = deque()

for el in line:
    orders.append(int(el))

print(max(orders))

while True:
    if not orders:
        break
    order = orders.popleft()
    if food >= order:
        food -= order
    else:
        orders.append(order)

if orders:
    print(f'Orders left: ', end='')
    print(orders.popleft())
else:
    print("Orders complete")