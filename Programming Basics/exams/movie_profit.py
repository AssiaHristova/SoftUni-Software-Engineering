movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percent_kept = int(input())

revenue = days * (tickets * ticket_price)
net_revenue = revenue - revenue * (percent_kept / 100)

print(f"The profit from the movie {movie} is {net_revenue:.2f} lv.")