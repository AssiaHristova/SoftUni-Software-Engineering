import math

year = input()
p = int(input())
h = int(input())

days = 0.0
weekends = 48
weekends_off_work = 3/4 * (48-h)

days_in_sofia = weekends_off_work + p * 2/3
days_in_hometown = h
days = days_in_sofia + h

if year == 'leap':
    days = days + days * 0.15

print(math.floor(days))
