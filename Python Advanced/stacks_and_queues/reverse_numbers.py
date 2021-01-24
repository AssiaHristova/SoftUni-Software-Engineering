nums = input().split()

stack_1 = []
result = ''

for num in nums:
    stack_1.append(num)

while stack_1:
    result += (stack_1.pop() + ' ')

print(result)
