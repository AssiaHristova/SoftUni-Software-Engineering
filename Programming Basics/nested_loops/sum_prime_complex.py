command = input()

sum_prime = 0
sum_complex = 0

while command != 'stop':
    number = int(command)
    if number == 1:
        sum_prime += 1
    elif number > 1:
        for n in range(2, number):
            if number % n == 0:
                sum_complex += number
                break
        else:
            sum_prime += number
    elif number < 0:
        print('Number is negative.')

    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_complex}')
