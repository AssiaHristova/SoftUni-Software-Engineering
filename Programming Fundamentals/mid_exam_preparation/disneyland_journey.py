journey_price = float(input())
months = int(input())

saved_money = 0

for month in range(1, months + 1):
    if not month % 2 == 0:
        if not month == 1:
            saved_money -= saved_money * 0.16
    if month % 4 == 0:
        saved_money += saved_money * 0.25

    saved_money += journey_price * 0.25

if saved_money >= journey_price:
    print(f"Bravo! You can go to Disneyland and you will have {(saved_money - journey_price):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(journey_price - saved_money):.2f}lv. more.")
