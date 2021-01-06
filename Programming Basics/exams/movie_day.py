shoot_time = int(input())
scenes = int(input())
scene_length = int(input())

preparation_time = shoot_time * 0.15
time_need = preparation_time + scenes * scene_length
time_out = shoot_time - time_need
time_more = time_need - shoot_time

if time_need <= shoot_time:
    print(f"You managed to finish the movie on time! You have {time_out:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {time_more:.0f} minutes.")