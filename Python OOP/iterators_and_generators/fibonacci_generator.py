def fibonacci():
    number = 0
    counter = 0
    current_sum = 0
    previous_number = 0
    while True:
        if number == 0 and counter == 1:
            number += 1
        elif number == 1 and counter == 2:
            previous_number = 0
        else:
            number = current_sum
        current_sum = number + previous_number

        counter += 1
        previous_number = number
        yield current_sum


generator = fibonacci()
for i in range(10):
    print(next(generator))
