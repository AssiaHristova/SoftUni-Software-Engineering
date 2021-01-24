line = input().split()
rack_capacity = int(input())

clothes = [int(el) for el in line]

sum_clothes = 0
racks = 1

while clothes:
    cloth = clothes.pop()
    sum_clothes += cloth
    if sum_clothes == rack_capacity:
        if clothes:
            racks += 1
            sum_clothes = 0
    elif sum_clothes > rack_capacity:
        racks += 1
        sum_clothes = cloth

print(racks)




