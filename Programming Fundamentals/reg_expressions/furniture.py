import re
data = input()

spend_money = 0
data_all = ''
furniture = {}

while not data == "Purchase":
    data_all += data
    data = input()

pattern = r'>>(?P<furniture>[a-zA-z]+)<<(?P<price>[0-9]+\.?[0-9]+)\!(?P<quantity>[0-9]+)'
results = re.finditer(pattern, data_all)

print("Bought furniture:")
for result in results:
    furniture = result.groupdict()
    spend_money += (float(furniture['price']) * int(furniture['quantity']))
    print(furniture['furniture'])
print(f"Total money spend: {spend_money:.2f}")



