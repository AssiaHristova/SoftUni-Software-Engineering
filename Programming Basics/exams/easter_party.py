guests = int(input())
couvert = float(input())
budget = float(input())

price = 0

if guests < 10:
    price = guests * couvert
elif 10 <= guests <= 15:
    price = guests * (couvert * 0.85)
elif 15 < guests <= 20:
    price = guests * (couvert * 0.80)
else:
    price = guests * (couvert * 0.75)

price_cake = budget * 0.10
total_price = price + price_cake

if budget >= total_price:
    print(f"It is party time! {(budget - total_price):.2f} leva left.")
else:
    print(f"No party! {(total_price - budget):.2f} leva needed.")