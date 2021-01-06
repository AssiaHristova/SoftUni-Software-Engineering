juniors = int(input())
seniors = int(input())
trail_type = input()

donated_money = 0
fee_juniors = 0
fee_seniors = 0

if trail_type == 'trail':
    fee_juniors = juniors * 5.50
    fee_seniors = seniors * 7
elif trail_type == 'cross-country':
    if juniors + seniors < 50:
        fee_juniors = juniors * 8
        fee_seniors = seniors * 9.50
    else:
        fee_juniors = (juniors * 8) * 75 / 100
        fee_seniors = (seniors * 9.50) * 75 / 100
elif trail_type == 'downhill':
    fee_juniors = juniors * 12.25
    fee_seniors = seniors * 13.75
else:
    fee_juniors = juniors * 20
    fee_seniors = seniors * 21.50

donated_money = (fee_juniors + fee_seniors) * 95 / 100
print(f'{donated_money:.2f}')