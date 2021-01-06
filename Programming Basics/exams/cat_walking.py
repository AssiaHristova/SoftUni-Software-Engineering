minutes_walking = int(input())
walks = int(input())
kalorees_taken = int(input())

kalorees_per_walk = minutes_walking * 5
kalorees_per_day = walks * kalorees_per_walk

if kalorees_per_day >= kalorees_taken / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {kalorees_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {kalorees_per_day}.")