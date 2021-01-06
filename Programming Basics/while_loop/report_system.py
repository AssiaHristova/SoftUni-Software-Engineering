donation_amount = int(input())
command = input()

card_payment = 0
cash_payment = 0
count = 0
total_payment = 0
total_cash = 0
total_card = 0
count_card = 0
count_cash = 0

while command != 'End':
    payment = int(command)
    count += 1
    if count % 2 == 0:
        card_payment = payment
        if card_payment < 10:
            print('Error in transaction!')
        else:
            total_card += payment
            count_card += 1
            print('Product sold!')
    else:
        cash_payment = payment
        if cash_payment > 100:
            print('Error in transaction!')
        else:
            total_cash += payment
            count_cash += 1
            print('Product sold!')
    total_payment = total_card + total_cash
    if total_payment >= donation_amount:
        break

    command = input()


if total_payment >= donation_amount:
    print(f'Average CS: {(total_cash / count_cash):.2f}')
    print(f'Average CC: {(total_card / count_card):.2f}')
else:
    print('Failed to collect required money for charity.')