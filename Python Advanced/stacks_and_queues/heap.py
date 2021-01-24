from heapq import *

heap = []  # the same as stack but remove them by value

heappush(heap, 1)
heappush(heap, -2)
heappush(heap, -10)
heappush(heap, 5)

print(heap)

while heap:
    print(heappop(heap))
