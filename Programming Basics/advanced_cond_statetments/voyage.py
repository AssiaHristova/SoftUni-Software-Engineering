budget = float(input())
season = input()

accommodation = ''
destination = ''
price = 0.0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.30
    else:
        price = budget * 0.70
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.40
    else:
        price = budget * 0.80
else:
    destination = 'Europe'
    price = budget * 0.90

if season == 'summer' and destination != 'Europe':
    accommodation = 'Camp'
else:
    accommodation = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation} - {price:.2f}')





