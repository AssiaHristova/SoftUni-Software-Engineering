import sys

gamer = input()

max_points = -sys.maxsize
winner = ''

while gamer != "Stop":
    points = 0
    for letter in gamer:
        number = int(input())
        number_1 = ord(letter)
        if number == number_1:
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner = gamer

    gamer = input()


print(f"The winner is {winner} with {max_points} points!")


