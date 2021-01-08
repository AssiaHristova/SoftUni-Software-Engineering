import re
line = input().split(', ')

demons = {}

health_pattern = r'[^0-9\+\-\*\/\.\,\s]'
damage_pattern = r'([\+\-\*\/]?)[0-9]+([\.\*\/\+\-]?)([0-9]?)+?([\*\/]?)+'

for demon in line:
    health = 0
    damage = 0
    multiply = 0
    division = 0
    health_data = re.findall(health_pattern, demon)
    for el in health_data:
        health += ord(el)
    damage_data = re.finditer(damage_pattern, demon)
    damage_info = [damage.group() for damage in damage_data]
    for ele in damage_info:
        if '*' in ele:
            n = ele.count('*')
            ele = ele.replace('*', '')
            multiply += n
        if '/' in ele:
            m = ele.count('/')
            ele = ele.replace('/', '')
            division += m
        ele = float(ele)
        damage += ele
    if multiply > 0:
        damage *= (multiply * 2)
    if division > 0:
        damage /= (division * 2)
    demons[demon] = [health, damage]

sorted_demons = sorted(demons.items(),key=lambda x: x[0])

for demon in sorted_demons:
    print(f"{demon[0]} - {demon[1][0]} health, {demon[1][1]:.2f} damage")





