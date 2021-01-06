import math

days = int(input())
food_have = float(input())
food_dog_per_day = float(input())
food_cat_per_day = float(input())
food_turtle_per_day = float(input())

total_food = days * (food_dog_per_day + food_cat_per_day + (food_turtle_per_day / 1000))

if food_have >= total_food:
    print(f'{math.floor(food_have - total_food )} kilos of food left.')
else:
    print(f'{math.ceil(total_food - food_have)} more kilos of food are needed.')