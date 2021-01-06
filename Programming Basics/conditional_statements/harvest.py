import math

X = int(input())
Y = float(input())
Z = int(input())
workers = int(input())

grapes = X * (40 / 100) * Y
wine = grapes / 2.5

if wine < Z:
    print(f'It will be a tough winter! More {math.floor(Z - wine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine)} liters.')
    print(f'{math.ceil(wine - Z)} liters left -> {math.ceil((wine - Z) / workers)} liters per person.')