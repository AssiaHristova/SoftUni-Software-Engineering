payment = input()

total_money = 0.0

while payment != 'NoMoreMoney':
    money = float(payment)
    if money < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {money:.2f}')
    total_money += money
    payment = input()

print(f'Total: {total_money:.2f}')


