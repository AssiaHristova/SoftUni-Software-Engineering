import re
import math
text = input()

total_calories = 0

pattern = r'(?P<separator>[#\|])(?P<item>[a-zA-Z\s]+)(?P=separator)(?P<expdate>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)'

food_info = re.finditer(pattern, text)
food_info_2 = re.finditer(pattern, text)

for el in food_info:
    foods = el.groupdict()
    total_calories += int(foods['calories'])

days = math.floor(total_calories / 2000)
print(f"You have food to last you for: {days} days!")

for el in food_info_2:
    f = el.groupdict()
    print(f"Item: {f['item']}, Best before: {f['expdate']}, Nutrition: {f['calories']}")








