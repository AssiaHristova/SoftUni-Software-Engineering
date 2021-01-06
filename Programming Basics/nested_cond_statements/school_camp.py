season = input()
group = input()
students = int(input())
nights = int(input())

price = 0
discounted_price = 0
sport = ''

if season == 'Winter':
    if group == 'boys':
        price = nights * students * 9.60
        sport = 'Judo'
    elif group == 'girls':
        price = nights * students * 9.60
        sport = 'Gymnastics'
    else:
        price = nights * students * 10
        sport = 'Ski'
elif season == 'Spring':
    if group == 'boys':
        price = nights * students * 7.20
        sport = 'Tennis'
    elif group == 'girls':
        price = nights * students * 7.20
        sport = 'Athletics'
    else:
        price = nights * students * 9.50
        sport = 'Cycling'
else:
    if group == 'boys':
        price = nights * students * 15
        sport = 'Football'
    elif group == 'girls':
        price = nights * students * 15
        sport = 'Volleyball'
    else:
        price = nights * students * 20
        sport = 'Swimming'

if students >= 50:
    discounted_price = price * 0.5
elif 20 <= students < 50:
    discounted_price = price * 0.85
elif 10 <= students < 20:
    discounted_price = price * 0.95
else:
    discounted_price = price


print(f'{sport} {discounted_price:.2f} lv.')