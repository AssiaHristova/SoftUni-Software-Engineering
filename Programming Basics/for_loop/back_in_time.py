heritage = float(input())
year_to_live = int(input())

spend_money = 0
money_out = 0

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        spend_money += 12000
    else:
        spend_money += 12000 + 50 * (i - 1800 + 18)

money_out = heritage - spend_money

if money_out >= 0:
    print(f"Yes! He will live a carefree life and will have {money_out:.2f} dollars left." )
else:
    print(f"He will need {abs(money_out):.2f} dollars to survive.")