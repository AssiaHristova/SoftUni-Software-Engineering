from collections import deque

green_light = int(input())
free_window = int(input())

END_COMMAND = "END"
GREEN_COMMAND = "green"
cars = deque()
count = 0

while True:
    crash = False
    car = input()
    if car == END_COMMAND:
        print("Everyone is safe.")
        print(f"{count} total cars passed the crossroads.")
        break
    elif car == GREEN_COMMAND:
        seconds = green_light
        while seconds:
            if cars:
                passing_car = cars.popleft()
                if seconds >= len(passing_car):
                    seconds -= len(passing_car)
                    count += 1
                else:
                    seconds += free_window
                    if seconds >= len(passing_car):
                        seconds -= len(passing_car)
                        count += 1
                        break
                    else:
                        crash = True
                        letters_to_pass = len(passing_car) - seconds
                        crashed_index = -letters_to_pass
                        print("A crash happened!")
                        print(f"{passing_car} was hit at {passing_car[crashed_index]}.")
                        break
            else:
                break
        if crash:
            break
    else:
        cars.append(car)











