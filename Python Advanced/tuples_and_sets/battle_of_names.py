n = int(input())

odd_nums = set()
even_nums = set()

for i in range(n):
    name = input()
    sum_ascii = 0
    for letter in name:
        ascii_value = ord(letter)
        sum_ascii += ascii_value

    devised_num = sum_ascii // (i + 1)
    if devised_num % 2 == 0:
        even_nums.add(devised_num)
    else:
        odd_nums.add(devised_num)

sum_odds = sum(odd_nums)
sum_evens = sum(even_nums)

if sum_odds == sum_evens:
    result = odd_nums.union(even_nums)
elif sum_odds > sum_evens:
    result = odd_nums.difference(even_nums)
else:
    result = odd_nums.symmetric_difference(even_nums)

result_list = [el for el in result]

for el in result_list:
    if el == result_list[-1]:
        print(el)
    else:
        print(el, end=', ')



