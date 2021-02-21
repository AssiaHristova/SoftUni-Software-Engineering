from collections import deque


def stock_availability(boxes, command, *args):
    boxes_queue = deque(boxes)
    if command == "delivery":
        new_boxes = args
        for el in new_boxes:
            boxes_queue.append(el)
            boxes = list(boxes_queue)
        return boxes
    elif command == "sell":
        if not args:
            boxes_queue.popleft()
            boxes = list(boxes_queue)
            return boxes
        else:
            sold_boxes = args
            if isinstance(sold_boxes[0], int):
                for _ in range(sold_boxes[0]):
                    boxes_queue.popleft()
                boxes = list(boxes_queue)
                return boxes
            elif isinstance(sold_boxes[0], str):
                for el in sold_boxes:
                    while el in boxes_queue:
                        boxes_queue.remove(el)
                boxes = list(boxes_queue)
                return boxes



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))



