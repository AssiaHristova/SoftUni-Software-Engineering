days = int(input())
budget = float(input())
people = int(input())
fuel_price_per_km = float(input())
food_price_per_day_per_person = float(input())
hotel_price_per_day_per_person = float(input())

food_expenses = food_price_per_day_per_person * people * days
hotel_expenses = hotel_price_per_day_per_person * people * days
if people > 10:
    hotel_expenses -= hotel_expenses * 0.25
total_expenses = food_expenses + hotel_expenses

for day in range(1, days + 1):
    distance = float(input())
    total_expenses += fuel_price_per_km * distance
    if day % 3 == 0 or day % 5 == 0:
        total_expenses += (total_expenses * 0.4)
    if day % 7 == 0:
        total_expenses -= (total_expenses / people)
    if total_expenses > budget:
        break

if total_expenses > budget:
    print(f"Not enough money to continue the trip. You need {(total_expenses - budget):.2f}$ more.")
if total_expenses <= budget:
    print(f"You have reached the destination. You have {(budget - total_expenses):.2f}$ budget left.")