command = input()

gross_price = 0
net_price = 0
total_price = 0
taxes = 0

while True:
    if command == "special":
        total_price = gross_price * 0.9
        break
    elif command == "regular":
        break
    else:
        if float(command) > 0:
            net_price += float(command)
            gross_price = (net_price * 1.2)
            total_price = gross_price
            taxes = (net_price * 0.2)
        else:
            print("Invalid price!")

    command = input()


if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print('-----------')
    print(f"Total price: {total_price:.2f}$")

