from collections import deque

water = int(input())

people = deque()

START_COMMAND = "Start"
END_COMMAND = "End"
REFILL_COMMAND = 'refill'

while True:
    name = input()
    if name == START_COMMAND:
        break
    else:
        people.append(name)


while True:
    command = input()
    if command == END_COMMAND:
        print(f"{water} liters left")
        break
    elif command.startswith(REFILL_COMMAND):
        refill = command.split()
        water += int(refill[1])
    else:
        person = people.popleft()
        if water >= int(command):
            water -= int(command)
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

