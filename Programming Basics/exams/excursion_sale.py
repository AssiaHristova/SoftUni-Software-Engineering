sea_count = int(input())
mountain_count = int(input())
packet_type = input()

price = 0

while packet_type != "Stop":
    if packet_type == "sea":
        if sea_count > 0:
            price += 680
            sea_count -= 1
    elif packet_type == "mountain":
        if mountain_count > 0:
            price += 499
            mountain_count -= 1
    if sea_count == 0 and mountain_count == 0:
        break

    packet_type = input()

if sea_count == 0 and mountain_count == 0:
    print("Good job! Everything is sold.")

print(f"Profit: {price} leva.")

