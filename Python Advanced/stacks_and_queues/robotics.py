from collections import deque
from datetime import datetime
from datetime import timedelta

line = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

def available_robot(available_robots):
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")


products = deque([])
robots = []
available_robots = deque([])

END_COMMAND = "End"

while True:
    product = input()
    if product == END_COMMAND:
        break
    else:
        products.append(product)

time += timedelta(seconds=1)

for el in line:
    data = el.split('-')
    robot = {}
    robot['name'] = data[0]
    robot['processing_time'] = int(data[1])
    robot['available_at'] = time
    robots.append(robot)
    available_robots.append(robot)


while products:
    current_product = products.popleft()
    if available_robots:
        available_robot(available_robots)
    else:
        for r in robots:
            if time >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            available_robot(available_robots)

    time += timedelta(seconds=1)










