budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards * 250
processor_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10

total_price = video_cards_price + processors * processor_price + ram * ram_price

if video_cards > processors:
    total_price = total_price * 0.85

money_out = budget - total_price

if budget >= total_price:
    print(f"You have {money_out:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(money_out):.2f} leva more!")
