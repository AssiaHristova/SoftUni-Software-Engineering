chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())

cost = chicken_menus * 10.35 + fish_menus * 12.40 + veggie_menus * 8.15
dessert = cost * 0.2
total_cost = cost + dessert + 2.50

print(f'Total: {total_cost:.2f}')

