budget = int(input())
season = input()
fisherman = int(input())

rent = 0.0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or \
        season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fisherman <= 6:
    rent = rent * 0.9
elif 7 <= fisherman <= 11:
    rent = rent * 0.85
elif fisherman >= 12:
    rent = rent * 0.75

if fisherman % 2 == 0 and season != 'Autumn':
    rent = rent * 0.95

money_out = abs(budget - rent)

if budget >= rent:
    print(f'Yes! You have {money_out:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_out:.2f} leva.')