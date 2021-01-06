price_flour = float(input())
flour = float(input())
sugar = float(input())
egg_packs = int(input())
yeast = int(input())

price_sugar = price_flour * 0.75
price_eggs = price_flour * 1.10
price_yeast = price_sugar * 0.20

total_price = flour * price_flour + sugar * price_sugar + egg_packs * price_eggs + yeast * price_yeast

print(f'{total_price:.2f}')

