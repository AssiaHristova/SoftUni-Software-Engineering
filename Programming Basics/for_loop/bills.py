months = int(input())

water_bill = 0
net_bill = 0
others_bill = 0
electricity_sum = 0
others_sum = 0
avg_bill = 0

for month in range(1, months + 1):
    electricity_bill = float(input())
    electricity_sum += electricity_bill
    water_bill = 20
    net_bill = 15
    others = electricity_bill + water_bill + net_bill
    others_bill = others * 1.2
    others_sum += others_bill
    avg_bill = (electricity_sum + water_bill * months + net_bill * months + others_sum) / months

print(f"Electricity: {electricity_sum:.2f} lv")
print(f"Water: {water_bill * months:.2f} lv")
print(f"Internet: {net_bill * months:.2f} lv")
print(f"Other: {others_sum:.2f} lv")
print(f"Average: {avg_bill:.2f} lv")
