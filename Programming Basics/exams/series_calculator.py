import math

series = input()
seasons = int(input())
episodes = int(input())
episode_length = float(input())

commercials = episode_length * 0.20
time_per_season = episodes * (episode_length + commercials) + 10
time_all = math. floor(seasons * time_per_season)

print(f"Total time needed to watch the {series} series is {time_all} minutes.")

