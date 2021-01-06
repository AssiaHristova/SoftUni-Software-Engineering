town = input()
sales = float(input())


if town == 'Sofia' and 0 <= sales <= 500:
    print(f'{sales * 5/100:.2f}')
elif town == 'Sofia' and 500 < sales <= 1000:
    print(f'{sales * 7/100:.2f}')
elif town == 'Sofia' and 1000 < sales <= 10000:
    print(f'{sales * 8/100:.2f}')
elif town == 'Sofia' and sales > 10000:
    print(f'{sales * 12/100:.2f}')
elif town == 'Varna' and 0 <= sales <= 500:
    print(f'{sales * 4.5/100:.2f}')
elif town == 'Varna' and 500 < sales <= 1000:
    print(f'{sales * 7.5/100:.2f}')
elif town == 'Varna' and 1000 < sales <= 10000:
    print(f'{sales * 10/100:.2f}')
elif town == 'Varna' and sales > 10000:
    print(f'{sales * 13/100:.2f}')
elif town == 'Plovdiv' and 0 <= sales <= 500:
    print(f'{sales * 5.5/100:.2f}')
elif town == 'Plovdiv' and 500 < sales <= 1000:
    print(f'{sales * 8/100:.2f}')
elif town == 'Plovdiv' and 1000 < sales <= 10000:
    print(f'{sales * 12/100:.2f}')
elif town == 'Plovdiv' and sales > 10000:
    print(f'{sales * 14.5/100:.2f}')
else:
    print('error')

