def factorial_num(num):
    fact_num = 1
    if num > 0:
        for i in range(1, num + 1):
            fact_num *= i
    return fact_num


number_1 = int(input())
number_2 = int(input())

result = (factorial_num(number_1) / factorial_num(number_2))
print(f'{result:.2f}')