n = int(input())

VIPs = set()
regular_guests = set()

for _ in range(n):
    reservation_num = input()
    first_symbol = reservation_num[0]
    if first_symbol.isdigit():
        VIPs.add(reservation_num)
    else:
        regular_guests.add(reservation_num)

command = input()

while not command == 'END':
    if command in VIPs:
        VIPs.remove(command)
    elif command in regular_guests:
        regular_guests.remove(command)

    command = input()

not_arrived = len(VIPs) + len(regular_guests)
print(not_arrived)

sorted_VIPs = sorted(VIPs)
sorted_regular_guests = sorted(regular_guests)

for guest in sorted_VIPs:
    print(guest)

for guest in sorted_regular_guests:
    print(guest)




