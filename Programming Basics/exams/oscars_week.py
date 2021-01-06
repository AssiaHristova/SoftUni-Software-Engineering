movie = input()
hall_type = input()
tickets = int(input())

revenue = 0

if movie == "A Star Is Born":
    if hall_type == "normal":
        revenue = tickets * 7.50
    elif hall_type == "luxury":
        revenue = tickets * 10.50
    else:
        revenue = tickets * 13.50
elif movie == "Bohemian Rhapsody":
    if hall_type == "normal":
        revenue = tickets * 7.35
    elif hall_type == "luxury":
        revenue = tickets * 9.45
    else:
        revenue = tickets * 12.75
elif movie == "Green Book":
    if hall_type == "normal":
        revenue = tickets * 8.15
    elif hall_type == "luxury":
        revenue = tickets * 10.25
    else:
        revenue = tickets * 13.25
else:
    if hall_type == "normal":
        revenue = tickets * 8.75
    elif hall_type == "luxury":
        revenue = tickets * 11.55
    else:
        revenue = tickets * 13.95

print(f"{movie} -> {revenue:.2f} lv.")

