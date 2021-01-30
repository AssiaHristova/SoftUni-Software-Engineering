phonebook = {}

while True:
    line = input()
    if line.isdigit():
        n = int(line)
        break

    else:
        data = line.split('-')
        name = data[0]
        phone = data[1]
        if name in phonebook:
            phonebook[name] = phone
        else:
            phonebook[name] = phone

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")