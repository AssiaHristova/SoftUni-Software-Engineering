days = int(input())
hours_per_day = int(input())

day_fee = 0
total_fee = 0

for i in range(1, days + 1):
    day_fee = 0
    for j in range(1, hours_per_day + 1):
        if i % 2 == 0 and j % 2 != 0:
            day_fee += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            day_fee += 1.25
        else:
            day_fee += 1

    total_fee += day_fee
    print(f"Day: {i} - {day_fee:.2f} leva")

print(f"Total: {total_fee:.2f} leva")