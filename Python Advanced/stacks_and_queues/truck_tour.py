from collections import deque

n = int(input())

stations = deque([])

for _ in range(n):
    data = input().split()
    stations.append([int(el) for el in data])

for big_circle_iteration in range(n):
    is_valid = True
    tank = 0
    for small_circle_iteration in range(n):
        tank += (stations[small_circle_iteration][0] - stations[small_circle_iteration][1])
        if tank < 0:
            is_valid = False
            stations.append(stations.popleft())
            break
    if is_valid:
        print(big_circle_iteration)
        break





