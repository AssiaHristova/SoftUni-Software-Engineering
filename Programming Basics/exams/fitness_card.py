budget = float(input())
gender = input()
age = int(input())
sport = input()

fitness_card = 0

if gender == 'm':
    if sport == 'Gym':
        fitness_card = 42
    elif sport == 'Boxing':
        fitness_card = 41
    elif sport == 'Yoga':
        fitness_card = 45
    elif sport == 'Zumba':
        fitness_card = 34
    elif sport == 'Dances':
        fitness_card = 51
    else:
        fitness_card = 39
else:
    if sport == 'Gym':
        fitness_card = 35
    elif sport == 'Boxing':
        fitness_card = 37
    elif sport == 'Yoga':
        fitness_card = 42
    elif sport == 'Zumba':
        fitness_card = 31
    elif sport == 'Dances':
        fitness_card = 53
    else:
        fitness_card = 37

if age <= 19:
    fitness_card = fitness_card * 0.80

if budget >= fitness_card:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${(fitness_card - budget):.2f} more.")
