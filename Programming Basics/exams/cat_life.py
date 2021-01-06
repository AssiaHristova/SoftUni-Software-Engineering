import math
breed = input()
gender = input()

cat_months = 0

if breed == "British Shorthair":
    if gender == 'm':
        cat_months = (13 * 12) / 6
    else:
        cat_months = (14 * 12) / 6
elif breed == "Siamese":
    if gender == 'm':
        cat_months = (15 * 12) / 6
    else:
        cat_months = (16 * 12) / 6
elif breed == "Persian":
    if gender == 'm':
        cat_months = (14 * 12) / 6
    else:
        cat_months = (15 * 12) / 6
elif breed == "Ragdoll":
    if gender == 'm':
        cat_months = (16 * 12) / 6
    else:
        cat_months = (17 * 12) / 6
elif breed == "American Shorthair":
    if gender == 'm':
        cat_months = (12 * 12) / 6
    else:
        cat_months = (13 * 12) / 6
elif breed == "Siberian":
    if gender == 'm':
        cat_months = (11 * 12) / 6
    else:
        cat_months = (12 * 12) / 6
else:
    cat_months = 0

if cat_months == 0:
    print(f'{breed} is invalid cat!')
else:
    print(f'{math.floor(cat_months)} cat months')

