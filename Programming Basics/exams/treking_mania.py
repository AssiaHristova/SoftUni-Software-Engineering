groups = int(input())

climbers = 0
moussalla = 0
montblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group in range(1, groups + 1):
    people_per_group = int(input())
    climbers += people_per_group
    if people_per_group <= 5:
        moussalla += people_per_group
    elif 6 <= people_per_group <= 12:
        montblan += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimanjaro += people_per_group
    elif 26 <= people_per_group <= 40:
        k2 += people_per_group
    else:
        everest += people_per_group

print(f'{(moussalla / climbers) * 100:.2f}%')
print(f'{(montblan / climbers) * 100:.2f}%')
print(f'{(kilimanjaro / climbers) * 100:.2f}%')
print(f'{(k2 / climbers) * 100:.2f}%')
print(f'{(everest / climbers) * 100:.2f}%')


