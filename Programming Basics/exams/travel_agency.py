town = input()
package_type = input()
vip = input()
days = int(input())

price = 0

if 1 <= days <= 7:
    if town == "Bansko" or town == "Borovets":
        if package_type == "withEquipment":
            if vip == "yes":
                price = (days * 100) * 0.90
            elif vip == "no":
                price = days * 100
            else:
                price = 0
        elif package_type == "noEquipment":
            if vip == "yes":
                price = (days * 80) * 0.95
            elif vip == "no":
                price = days * 80
            else:
                price = 0
        else:
            price = 0
    elif town == "Varna" or town == "Burgas":
        if package_type == "withBreakfast":
            if vip == "yes":
                price = (days * 130) * 0.88
            elif vip == "no":
                price = days * 130
            else:
                price = 0
        elif package_type == "noBreakfast":
            if vip == "yes":
                price = (days * 100) * 0.93
            elif vip == "no":
                price = days * 100
            else:
                price = 0
        else:
            price = 0
elif days > 7:
    if town == "Bansko" or town == "Borovets":
        if package_type == "withEquipment":
            if vip == "yes":
                price = ((days - 1) * 100) * 0.90
            elif vip == "no":
                price = (days - 1) * 100
            else:
                price = 0
        elif package_type == "noEquipment":
            if vip == "yes":
                price = ((days - 1) * 80) * 0.95
            elif vip == "no":
                price = (days - 1) * 80
            else:
                price = 0
        else:
            price = 0
    elif town == "Varna" or town == "Burgas":
        if package_type == "withBreakfast":
            if vip == "yes":
                price = ((days - 1) * 130) * 0.88
            elif vip == "no":
                price = (days - 1) * 130
            else:
                price = 0
        elif package_type == "noBreakfast":
            if vip == "yes":
                price = ((days - 1) * 100) * 0.93
            elif vip == "no":
                price = (days - 1) * 100
            else:
                price = 0
        else:
            price = 0
else:
    price = -10

if price == 0:
    print("Invalid input!")
elif price < 0:
    print("Days must be positive number!")
else:
    print(f"The price is {price:.2f}lv! Have a nice time!")


