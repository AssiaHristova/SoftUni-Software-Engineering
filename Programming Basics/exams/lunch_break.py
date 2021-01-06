import math

series = input()
episode_length = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

time_left = break_time - lunch_time - rest_time
time_out = math.ceil(abs(time_left - episode_length))

if time_left >= episode_length:
    print(f"You have enough time to watch {series} and left with {time_out} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {time_out} more minutes.")
