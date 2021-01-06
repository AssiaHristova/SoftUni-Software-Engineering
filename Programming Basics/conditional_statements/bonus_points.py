base_points = int(input())

if base_points <= 100:
    bonus_points = 5
elif 1000 >= base_points > 100:
    bonus_points = base_points * 20/100
else:
    bonus_points = base_points * 10/100

if base_points % 2 == 0:
    extra_points = 1
elif base_points % 5 == 0:
    extra_points = 2
else:
    extra_points = 0

total_points = base_points + bonus_points + extra_points

print(bonus_points + extra_points)
print(total_points)

