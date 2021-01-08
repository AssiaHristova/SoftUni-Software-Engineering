def perfect_number(num):
    aliquot_sum = 0
    if num > 0:
        for i in range(1, num):
            if num % i == 0:
                aliquot_sum += i
    if num == aliquot_sum:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


integer = int(input())
perfect_number(integer)





