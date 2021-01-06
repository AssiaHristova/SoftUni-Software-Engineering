import sys

eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = -sys.maxsize
color_max = ''

for egg in range(1, eggs + 1):
    color = input()
    if color == 'red':
        red_eggs += 1
        if red_eggs > max_eggs:
            max_eggs = red_eggs
            color_max = 'red'
    elif color == 'orange':
        orange_eggs += 1
        if orange_eggs > max_eggs:
            max_eggs = orange_eggs
            color_max = 'orange'
    elif color == 'blue':
        blue_eggs += 1
        if blue_eggs > max_eggs:
            max_eggs = blue_eggs
            color_max = 'blue'
    else:
        green_eggs += 1
        if green_eggs > max_eggs:
            max_eggs = green_eggs
            color_max = 'green'

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {color_max}")
