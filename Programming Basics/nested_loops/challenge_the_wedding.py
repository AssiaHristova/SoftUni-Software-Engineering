men = int(input())
women = int(input())
max_tables = int(input())

count_men = 0
count_women = 0
tables = 0

for man in range(1, men + 1):
    count_men += 1
    count_women = 0
    for woman in range(1, women + 1):
        count_women += 1
        tables += 1
        if tables > max_tables:
            break
        print(f'({count_men} <-> {count_women})', end=' ')

