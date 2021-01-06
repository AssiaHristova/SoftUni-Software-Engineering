import  math

rest_days = int(input())

play_min_rest = rest_days * 127
play_min_work = (365 - rest_days) * 63
play_mins = play_min_rest + play_min_work
minutes_out = 30000 - play_mins
H = math.floor(abs(minutes_out) / 60)
M = abs(minutes_out) % 60

if minutes_out < 0:
    print('Tom will run away')
    print(f'{H} hours and {M} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{H} hours and {M} minutes less for play')