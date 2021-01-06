movie = input()
movie_package = input()
tickets = int(input())

price = 0

if movie == "John Wick":
    if movie_package == "Drink":
        price = tickets * 12
    elif movie_package == "Popcorn":
        price = tickets * 15
    else:
        price = tickets * 19
elif movie == "Star Wars":
    if tickets < 4:
        if movie_package == "Drink":
            price = tickets * 18
        elif movie_package == "Popcorn":
            price = tickets * 25
        else:
            price = tickets * 30
    else:
        if movie_package == "Drink":
            price = (tickets * 18) * 0.70
        elif movie_package == "Popcorn":
            price = (tickets * 25) * 0.70
        else:
            price = (tickets * 30) * 0.70
else:
    if tickets != 2:
        if movie_package == "Drink":
            price = tickets * 9
        elif movie_package == "Popcorn":
            price = tickets * 11
        else:
            price = tickets * 14
    else:
        if movie_package == "Drink":
            price = (tickets * 9) * 0.85
        elif movie_package == "Popcorn":
            price = (tickets * 11) * 0.85
        else:
            price = (tickets * 14) * 0.85

print(f"Your bill is {price:.2f} leva.")

