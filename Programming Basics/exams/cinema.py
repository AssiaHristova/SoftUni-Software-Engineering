capacity = int(input())
command = input()

seats = 0
total_price = 0

while command != "Movie time!":
    visitors = int(command)
    seats += visitors
    if seats > capacity:
        break
    if visitors % 3 == 0:
        total_price += (visitors * 5) - 5
    else:
        total_price += (visitors * 5)

    command = input()

if command == "Movie time!":
    print(f"There are {capacity - seats} seats left in the cinema.")
else:
    print("The cinema is full.")

print(f"Cinema income - {total_price} lv.")



