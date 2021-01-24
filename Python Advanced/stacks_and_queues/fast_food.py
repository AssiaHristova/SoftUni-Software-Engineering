from collections import deque

food = int(input())
line = input().split()

orders_left = []
orders = deque()

for el in line:
    orders.append(int(el))

print(max(orders))

while orders:
    order = orders.popleft()
    if food > order:
        food -= order
    elif food == order:
        break
    else:
        orders_left.append(order)

if orders_left:
    print(f'Orders left: ', end='')
    print(*orders_left)
else:
    print("Orders complete")




