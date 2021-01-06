import sys

movie = input()

max_points = -sys.maxsize
max_movie = ''
count = 0

while movie != "STOP":
    count += 1
    points = 0
    length = len(movie)
    if count == 7:
        break
    for letter in movie:
        points += ord(letter)
        if 97 <= ord(letter) <= 122:
            points -= (length * 2)
        elif 65 <= ord(letter) <= 90:
            points -= length
    if points > max_points:
        max_points = points
        max_movie = movie

    movie = input()

if count == 7:
    print("The limit is reached.")

print(f"The best movie for you is {max_movie} with {max_points} ASCII sum.")
