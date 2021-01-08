import math
elements = input().split()
command = input()

count = 0
match_element = ''


while not command == "end":
    indexes = [int(index) for index in command.split()]
    count += 1
    flag = True
    if indexes[0] == indexes[1] or indexes[0] not in range(0, len(elements)) or indexes[1] not in range(0, len(elements)):
        elements.insert(math.ceil(len(elements) / 2), f"-{count}a")
        elements.insert(math.ceil(len(elements) / 2), f"-{count}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[indexes[0]] == elements[indexes[1]]:
            match_element = elements[indexes[0]]
            elements.remove(match_element)
            elements.remove(match_element)
            print(f"Congrats! You have found matching elements - {match_element}!")
            if len(elements) == 0:
                print(f"You have won in {count} turns!")
                break
        else:
            print("Try again!")

    command = input()

if command == 'end':
    print("Sorry you lose :(")
    print(' '.join(elements))
