season = input()
km_per_month = float(input())

revenue = 0
net_revenue = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        revenue = km_per_month * 4 * 0.75
    elif season == 'Summer':
        revenue = km_per_month * 4 * 0.90
    else:
        revenue = km_per_month * 4 * 1.05
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        revenue = km_per_month * 4 * 0.95
    elif season == 'Summer':
        revenue = km_per_month * 4 * 1.10
    else:
        revenue = km_per_month * 4 * 1.25
elif 10000 < km_per_month <= 20000:
    revenue = km_per_month * 4 * 1.45

net_revenue = revenue * 0.90

print(f'{net_revenue:.2f}')



