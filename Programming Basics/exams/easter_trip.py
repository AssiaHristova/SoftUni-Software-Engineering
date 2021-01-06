destination = input()
dates = input()
nights = int(input())

price = 0

if destination == 'France':
    if dates == '21-23':
        price = nights * 30
    elif dates == '24-27':
        price = nights * 35
    else:
        price = nights * 40
elif destination == 'Italy':
    if dates == '21-23':
        price = nights * 28
    elif dates == '24-27':
        price = nights * 32
    else:
        price = nights * 39
else:
    if dates == '21-23':
        price = nights * 32
    elif dates == '24-27':
        price = nights * 37
    else:
        price = nights * 43

print(f"Easter trip to {destination} : {price:.2f} leva.")