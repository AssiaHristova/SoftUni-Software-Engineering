import re
text = input()

travel_points = 0
destination = ''
destinations = []

pattern = r'(?P<separator>[=\/])[A-Z][a-zA-Z]{2,}(?P=separator)'

locations = re.finditer(pattern, text)

locations = [loc.group() for loc in locations]

for loc in locations:
    destination = loc[1:-1]
    travel_points += len(destination)
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
