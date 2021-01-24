from collections import deque

N = int(input())

pumps = deque()
tank = 0

for i in range(N):
    pumps.append(i)

for i in range(N):
    line = input().split()
    petrol = int(line[0])
    distance_to_next_pump = int(line[1])
    pump = pumps.popleft()
    if distance_to_next_pump < (tank + petrol):
        tank += petrol
        tank -= distance_to_next_pump
        first_pump = pump
        print(first_pump)










