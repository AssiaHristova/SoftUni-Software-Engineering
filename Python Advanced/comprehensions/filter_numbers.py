start_num = int(input())
end_num = int(input())

result = [x for x in range(start_num, end_num + 1) if any(x % i == 0 for i in range(2, 11))]

print(result)

print(any([False, False, True, False]))

