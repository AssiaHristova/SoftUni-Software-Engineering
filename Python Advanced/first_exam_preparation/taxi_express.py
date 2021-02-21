from collections import deque

customers = [int(customer) for customer in input().split(", ")]
taxis = [int(taxi) for taxi in input().split(", ")]

customers_queue = deque(customers)
total_time = 0

while customers_queue:
    if not taxis:
        break
    customer = customers_queue.popleft()
    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customer
    else:
        customers_queue.appendleft(customer)

if not customers_queue:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(customer) for customer in customers_queue])}')
