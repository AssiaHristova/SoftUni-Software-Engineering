command = input()

goal = 10000
steps = 0
steps_out = 0
steps_all = 0

while command != 'Going home':
    steps = int(command)
    steps_all += steps
    steps_out = goal - steps_all
    if steps_out <= 0:
        break

    command = input()

if command == 'Going home':
    steps_home = int(input())
    steps_all += steps_home
    steps_out = goal - steps_all


if steps_out <= 0:
    print('Goal reached! Good job!')
    print(f'{abs(steps_out)} steps over the goal!')
else:
    print(f"{steps_out} more steps to reach goal.")