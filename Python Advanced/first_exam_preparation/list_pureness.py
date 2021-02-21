from collections import deque


def best_list_pureness(nums, k):
    numbers = deque(nums)

    def list_pureness(numbers):
        pureness = 0
        for i in range(len(numbers)):
            pureness += numbers[i] * i
        return pureness

    max_pureness = list_pureness(numbers)
    rotation = 0
    max_rotation = 0

    for j in range(k):
        num_to_rotate = numbers.pop()
        numbers.appendleft(num_to_rotate)
        pureness = list_pureness(numbers)
        rotation += 1
        if pureness > max_pureness:
            max_pureness = pureness
            max_rotation = rotation

    return f"Best pureness {max_pureness} after {max_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
