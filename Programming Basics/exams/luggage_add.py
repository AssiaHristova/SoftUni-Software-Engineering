price_extra_lug = float(input())
lug_kilos = float(input())
days = int(input())
lug_count = int(input())

fee = 0
price = 0

if lug_kilos < 10:
    fee = price_extra_lug * 0.2
elif 10 <= lug_kilos <= 20:
    fee = price_extra_lug  * 0.5
else:
    fee = price_extra_lug

if days > 30:
    price = (lug_count * fee) * 1.10
elif 30 >= days > 7:
    price = (lug_count * fee) * 1.15
else:
    price = (lug_count * fee) * 1.4

print(f"The total price of bags is: {price:.2f} lv. ")


