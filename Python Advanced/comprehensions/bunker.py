categories = input().split(', ')
n = int(input())

items = {category: [] for category in categories}
count = 0
quality_sum = 0

for _ in range(n):
    data = input().split(' - ')
    category, item_name, values = data
    quantity_values = values.split(';')
    item_quantity = quantity_values[0].split(':')
    item_quality = quantity_values[1].split(':')
    quantity = int(item_quantity[1])
    quality = int(item_quality[1])
    if category in items:
        if items[category]:
            if item_name not in items[category][0]:
                items[category][0].append(item_name)
                items[category][1].append(quantity)
                items[category][2].append(quality)
            else:
                items[category][1] += quantity
        else:
            items[category] = [item_name], [quantity], [quality]

for category, (item_name, quantity, quality) in items.items():
    count += sum(quantity)
    quality_sum += sum(quality)

print(f"Count of items: {count}")
print(f"Average quality: {(quality_sum/len(items)):.2f}")

for category, (item_name, quantity, quality) in items.items():
    print(f"{category} -> {', '.join(item_name)}")






