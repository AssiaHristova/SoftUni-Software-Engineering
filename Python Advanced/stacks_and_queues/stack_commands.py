stack = []

stack.append(22)
stack.append(3)
stack.append(-9)
stack.append(12)

while stack:
    print(stack.pop())


class Stack:
    def __init__(self):
        self.internal_stack = []

    def push(self, value):
        self.internal_stack.append(value)

    def pop(self):
        return self.internal_stack.pop()

    def peek(self):
        return self.internal_stack[-1]

s2 = Stack()
s2.pop()
s2.push(3)
s2.peek()