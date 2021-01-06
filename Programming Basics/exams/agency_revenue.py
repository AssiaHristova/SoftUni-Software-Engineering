airline = input()
adult_tickets = int(input())
kid_tickets = int(input())
price_adult = float(input())
customer_fee = float(input())

price_kid = price_adult * 0.3

price = adult_tickets * (price_adult + customer_fee) + kid_tickets * (price_kid + customer_fee)
profit = price * 0.2



print(f"The profit of your agency from {airline} tickets is {profit:.2f} lv.")

