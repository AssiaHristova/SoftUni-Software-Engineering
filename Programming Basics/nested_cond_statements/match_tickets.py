budget = float(input())
ticket_type = input()
fans = int(input())

ticket_price = 0
money_out = 0

if ticket_type == 'VIP':
    ticket_price = fans * 499.99
    if 1 <= fans <= 4:
        budget = budget * 25 / 100
    elif 5 <= fans <= 9:
        budget = budget * 40 / 100
    elif 10 <= fans <= 24:
        budget = budget * 50 / 100
    elif 25 <= fans <= 49:
        budget = budget * 60 / 100
    else:
        budget = budget * 75 / 100
else:
    ticket_price = fans * 249.99
    if 1 <= fans <= 4:
        budget = budget * 25 / 100
    elif 5 <= fans <= 9:
        budget = budget * 40 / 100
    elif 10 <= fans <= 24:
        budget = budget * 50 / 100
    elif 25 <= fans <= 49:
        budget = budget * 60 / 100
    else:
        budget = budget * 75 / 100

money_out = budget - ticket_price

if money_out >= 0:
    print(f'Yes! You have {money_out:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(money_out):.2f} leva.')
