fruit = input()
day = input()
quantity = float(input())

if fruit == 'banana' and day == 'Monday' or \
        fruit == 'banana' and day == 'Tuesday' or \
        fruit == 'banana' and day == 'Wednesday' or \
        fruit == 'banana' and day == 'Thursday' or \
        fruit == 'banana' and day == 'Friday':
    print(f'{quantity * 2.50:.2f}')
elif fruit == 'banana' and day == 'Saturday' or \
        fruit == 'banana' and day == 'Sunday':
    print(f'{quantity * 2.70:.2f}')
elif fruit == 'apple' and day == 'Monday' or \
        fruit == 'apple' and day == 'Tuesday' or \
        fruit == 'apple' and day == 'Wednesday' or \
        fruit == 'apple' and day == 'Thursday' or \
        fruit == 'apple' and day == 'Friday':
    print(f'{quantity * 1.20:.2f}')
elif fruit == 'apple' and day == 'Saturday' or \
        fruit == 'apple' and day == 'Sunday':
    print(f'{quantity * 1.25:.2f}')
elif fruit == 'orange' and day == 'Monday' or \
        fruit == 'orange' and day == 'Tuesday' or \
        fruit == 'orange' and day == 'Wednesday' or \
        fruit == 'orange' and day == 'Thursday' or \
        fruit == 'orange' and day == 'Friday':
    print(f'{quantity * 0.85:.2f}')
elif fruit == 'orange' and day == 'Saturday' or \
        fruit == 'orange' and day == 'Sunday':
    print(f'{quantity * 0.90:.2f}')
elif fruit == 'grapefruit' and day == 'Monday' or \
        fruit == 'grapefruit' and day == 'Tuesday' or \
        fruit == 'grapefruit' and day == 'Wednesday' or \
        fruit == 'grapefruit' and day == 'Thursday' or \
        fruit == 'grapefruit' and day == 'Friday':
    print(f'{quantity * 1.45:.2f}')
elif fruit == 'grapefruit' and day == 'Saturday' or \
        fruit == 'grapefruit' and day == 'Sunday':
    print(f'{quantity * 1.60:.2f}')
elif fruit == 'kiwi' and day == 'Monday' or \
        fruit == 'kiwi' and day == 'Tuesday' or \
        fruit == 'kiwi' and day == 'Wednesday' or \
        fruit == 'kiwi' and day == 'Thursday' or \
        fruit == 'kiwi' and day == 'Friday':
    print(f'{quantity * 2.70:.2f}')
elif fruit == 'kiwi' and day == 'Saturday' or \
        fruit == 'kiwi' and day == 'Sunday':
    print(f'{quantity * 3.00:.2f}')
elif fruit == 'pineapple' and day == 'Monday' or \
        fruit == 'pineapple' and day == 'Tuesday' or \
        fruit == 'pineapple' and day == 'Wednesday' or \
        fruit == 'pineapple' and day == 'Thursday' or \
        fruit == 'pineapple' and day == 'Friday':
    print(f'{quantity * 5.50:.2f}')
elif fruit == 'pineapple' and day == 'Saturday' or \
        fruit == 'pineapple' and day == 'Sunday':
    print(f'{quantity * 5.60:.2f}')
elif fruit == 'grapes' and day == 'Monday' or \
        fruit == 'grapes' and day == 'Tuesday' or \
        fruit == 'grapes' and day == 'Wednesday' or \
        fruit == 'grapes' and day == 'Thursday' or \
        fruit == 'grapes' and day == 'Friday':
    print(f'{quantity * 3.85:.2f}')
elif fruit == 'grapes' and day == 'Saturday' or \
        fruit == 'grapes' and day == 'Sunday':
    print(f'{quantity * 4.20:.2f}')
else:
    print('error')
