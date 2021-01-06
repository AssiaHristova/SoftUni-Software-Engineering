bitcoins = int(input())
yuans = float(input())
commission = float(input())

bitcoins_to_leva = bitcoins * 1168
bitcoins_to_euro = bitcoins_to_leva / 1.95
yuans_to_dollars = yuans * 0.15
yuans_to_leva = yuans_to_dollars * 1.76
yuans_to_euro = yuans_to_leva / 1.95

euro = bitcoins_to_euro + yuans_to_euro
money = euro - euro * (commission / 100)

print(f'{money:.2f}')

