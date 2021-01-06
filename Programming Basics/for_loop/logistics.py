cargo_count = int(input())

avg_cost_per_tone = 0
transport_cost = 0
cargo_all = 0
bus_share = 0
truck_share = 0
train_share = 0

for cargo in range(1, cargo_count + 1):
    tonnage = int(input())
    cargo_all += tonnage
    if tonnage <= 3:
        transport_cost += tonnage * 200
        bus_share += tonnage
    elif 4 <= tonnage <= 11:
        transport_cost += tonnage * 175
        truck_share += tonnage
    else:
        transport_cost += tonnage * 120
        train_share += tonnage

    avg_cost_per_tone = transport_cost / cargo_all

print(f'{avg_cost_per_tone:.2f}')
print(f'{(bus_share / cargo_all) * 100:.2f}%')
print(f'{(truck_share / cargo_all) * 100:.2f}%')
print(f'{(train_share / cargo_all) * 100:.2f}%')
