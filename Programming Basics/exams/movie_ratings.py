import sys

movies_count = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
max_movie = ''
min_movie = ''
avg_rating = 0

for i in range(1, movies_count + 1):
    movie = input()
    rating = float(input())
    avg_rating += rating
    if rating > max_rating:
        max_rating = rating
        max_movie = movie
    if rating < min_rating:
        min_rating = rating
        min_movie = movie

print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {(avg_rating / movies_count):.1f}")