from collections import deque
from datetime import datetime


def deque_queue_test():
    q = deque()
    for i in range(1 << 20):
        q.append(i)
    while q:
        x = q.popleft()


def list_queue_test():
    q = []
    for i in range(1 << 20):
        q.append(i)
    while q:
        x = q.pop()


def measure(action):
    start_time = datetime.now()
    action()
    end_time = datetime.now()
    print(f'Finished in {end_time - start_time}')


measure(deque_queue_test)
measure(list_queue_test)


