n = int(input())

capacity = 255
total_liters = 0

for line in range(n):
    liters = int(input())
    total_liters += liters
    if total_liters > capacity:
        total_liters -= liters
        print("Insufficient capacity!")

print(total_liters)

