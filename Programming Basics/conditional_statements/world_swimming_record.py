import math

time_to_beat = float(input())
distance = float(input())
time_per_meter = float(input())

water_resistance = math.floor(distance/15)
ivan_time = distance * time_per_meter + water_resistance * 12.5

seconds_out = ivan_time - time_to_beat

if ivan_time < time_to_beat:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {seconds_out:.2f} seconds slower.')
