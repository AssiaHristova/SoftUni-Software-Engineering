price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

price_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

number_toys = number_puzzles + number_bears + number_dolls + number_minions + number_trucks

price_total = number_puzzles * price_puzzle + number_dolls * price_doll + number_minions * price_minion + number_bears * price_bear + number_trucks * price_truck

if number_toys >= 50:
    price_total = price_total * 75/100

rent = price_total * 10/100
revenue = price_total * 90/100
money_left = abs(revenue - price_excursion)

if revenue >= price_excursion:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')

