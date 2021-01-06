food = int(input())
command = input()

food_eaten = 0

while command != 'Adopted':
    food_per_meal = int(command)
    food_eaten += food_per_meal

    command = input()

if food_eaten <= food * 1000:
    print(f"Food is enough! Leftovers: {(food * 1000) - food_eaten} grams.")
else:
    print(f"Food is not enough. You need {food_eaten - (food * 1000)} grams more.")