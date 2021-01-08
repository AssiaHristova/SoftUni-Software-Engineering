n = int(input())

users = {}

for i in range(n):
    command = input().split()
    if 'register' in command:
        username = command[1]
        plate_num = command[2]
        if not username in users:
            users[username] = plate_num
            print(f"{username} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")
    elif 'unregister' in command:
        username = command[1]
        if username in users:
            users.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, plate_num in users.items():
    print(f"{username} => {plate_num}")

