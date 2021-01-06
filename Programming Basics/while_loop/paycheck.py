commission = input()

total = 0

while commission != 'End':
    cash = int(commission)
    total += cash

    commission = input()

print(f'{total}')
print(f'{total * 0.35}')

