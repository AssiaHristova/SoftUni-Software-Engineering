import re

line = input()

income = 0

pattern = r'%(?P<customer>[A-Z][a-z]+)%([^\|\$\.]?)+<(?P<product>\w+)>([^\|\$\.]?)+\|(?P<count>[0-9]+)\|([^\|\$\.[0-9]?)+(?P<price>[0-9]+\.?[0-9]+)\$'

while not line == "end of shift":
    data = re.finditer(pattern, line)
    for el in data:
        p = el.groupdict()
        customer = p['customer']
        product = p['product']
        count = int(p['count'])
        price = float(p['price'])
        total_price = count * price
        income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")

    line = input()

print(f"Total income: {income:.2f}")