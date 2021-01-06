import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

profit = magnolias * 3.25 + hyacinths * 4 + roses * 3.50 + cacti * 8
net_profit = profit * 95 / 100

if profit >= gift_price:
    print(f'She is left with {math.floor(net_profit - gift_price)} leva.')
else:
    print(f'She will have to borrow {math.ceil(gift_price - net_profit)} leva.')


