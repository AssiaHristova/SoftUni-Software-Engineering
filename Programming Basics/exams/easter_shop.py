eggs_quantity = int(input())
command = input()

eggs = 0
eggs_sold = 0
eggs_filled = 0

while command != 'Close':
    eggs = int(input())
    if command == 'Buy':
        if eggs > eggs_quantity:
            break
        else:
            eggs_sold += eggs
            eggs_quantity -= eggs
    elif command == 'Fill':
        eggs_filled += eggs
        eggs_quantity += eggs

    command = input()

if command == 'Close':
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_quantity}.")