egg_type = input()
egg_color = input()
batches = int(input())

revenue = 0
net_revenue = 0

if egg_type == 'Large':
    if egg_color == 'Red':
        revenue = batches * 16
    elif egg_color == 'Green':
        revenue = batches * 12
    else:
        revenue = batches * 9
elif egg_type == 'Medium':
    if egg_color == 'Red':
        revenue = batches * 13
    elif egg_color == 'Green':
        revenue = batches * 9
    else:
        revenue = batches * 7
else:
    if egg_color == 'Red':
        revenue = batches * 9
    elif egg_color == 'Green':
        revenue = batches * 8
    else:
        revenue = batches * 5

net_revenue = revenue * 0.65

print(f"{net_revenue:.2f} leva.")

