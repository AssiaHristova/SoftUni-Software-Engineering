days = int(input())
total_food = float(input())

biscuits = 0
food_per_day = 0
food_eaten = 0
food_eaten_dog = 0
food_eaten_cat = 0

for day in range(1, days + 1):
    food_dog = int(input())
    food_cat = int(input())
    food_per_day = food_dog + food_cat
    food_eaten_dog += food_dog
    food_eaten_cat += food_cat
    if day % 3 == 0:
        biscuits += food_per_day * 0.10

food_eaten = food_eaten_dog + food_eaten_cat
food_eaten_share = (food_eaten / total_food) * 100
food_eaten_dog_share = (food_eaten_dog / food_eaten) * 100
food_eaten_cat_share = (food_eaten_cat / food_eaten) * 100


print(f"Total eaten biscuits: {biscuits:.0f}gr.")
print(f"{food_eaten_share:.2f}% of the food has been eaten.")
print(f"{food_eaten_dog_share:.2f}% eaten from the dog.")
print(f"{food_eaten_cat_share:.2f}% eaten from the cat.")