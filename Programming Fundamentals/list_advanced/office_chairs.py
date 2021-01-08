n = int(input())

free_chairs = 0
rooms_count = 0
needed_chairs_in_room = 0

for room in range(n):
    rooms_count += 1
    chairs_count = 0
    command = input().split()
    chairs = str(command[0])
    for chair in chairs:
        if chair == "X":
            chairs_count += 1
    if chairs_count - int(command[-1]) >= 0:
        free_chairs += (chairs_count - int(command[-1]))
    else:
        needed_chairs_in_room = int(command[-1]) - chairs_count
        print(f"{needed_chairs_in_room} more chairs needed in room {rooms_count}")

if needed_chairs_in_room == 0:
    print(f"Game On, {free_chairs} free chairs left")