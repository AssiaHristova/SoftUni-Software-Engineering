vacation_money = float(input())
available_money = float(input())

days = 0
days_spend = 0

while available_money < vacation_money:
    command = input()
    current_money = float(input())
    days += 1
    if command == 'spend':
        days_spend += 1
        if days_spend == 5:
            break
        available_money -= current_money
        if available_money < 0:
            available_money = 0
    else:
        available_money += current_money
        days_spend = 0

if days_spend == 5:
    print("You can't save the money.")
    print(days)
else:
    print(f'You saved the money for {days} days.')
