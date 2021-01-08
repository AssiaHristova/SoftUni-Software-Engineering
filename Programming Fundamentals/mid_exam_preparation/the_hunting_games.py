N = int(input())
players = int(input())
energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

water = water_per_day_per_person * N * players
food = food_per_day_per_person * N * players

for day in range(1, N + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        break
    if day % 2 == 0:
        energy += energy * 0.05
        water -= water * 0.3
    if day % 3 == 0:
        food -= (food / players)
        energy += energy * 0.1

if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")


