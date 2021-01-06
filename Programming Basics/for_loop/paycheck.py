n = int(input())
paycheck = int(input())

for i in range(n):
    tab = input()
    if tab == 'Facebook':
        paycheck -= 150
    elif tab == 'Instagram':
        paycheck -= 100
    elif tab == 'Reddit':
        paycheck -= 50
    if paycheck <= 0:
        break

if paycheck > 0:
    print(paycheck)
else:
    print('You have lost your salary.')


