days = int(input())

total_money = 0
winner = 0
looser = 0

for day in range(1, days + 1):
    money_per_day = 0
    count_win = 0
    count_loose = 0
    sport = input()
    while sport != 'Finish':
        result = input()
        if result == 'win':
            money_per_day += 20
            count_win += 1
        else:
            count_loose += 1

        sport = input()

    if count_win > count_loose:
        winner += 1
        money_per_day = money_per_day * 1.10
    else:
        looser += 1
    total_money += money_per_day


if winner >= looser:
    print(f"You won the tournament! Total raised money: {(total_money * 1.20):.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")



