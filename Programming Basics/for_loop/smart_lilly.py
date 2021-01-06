n = int(input())
washm_price = float(input())
price_per_toy = int(input())

money = 0
money_toys = 0
money_brother = 0
count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        count += 1
        money += count * 10.00
        money_brother = money - count * 1.00
    else:
        money_toys += price_per_toy


money_all = money_brother + money_toys

if money_all >= washm_price:
    print(f'Yes! {money_all - washm_price:.2f}')
else:
    print(f'No! {washm_price - money_all:.2f}')


