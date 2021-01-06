exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time_m = exam_hour * 60 + exam_min
arrival_time_m = arrival_hour * 60 + arrival_min
min_out = exam_time_m - arrival_time_m

if 0 <= min_out <= 30:
    print('On time')
elif min_out < 0:
    print('Late')
elif min_out > 30:
    print('Early')

if min_out != 0:
    if 0 < min_out < 60:
        print(f'{min_out} minutes before the start')
    elif min_out >= 60:
        if min_out % 60 < 10:
            print(f'{min_out // 60}:0{min_out % 60} hours before the start')
        else:
            print(f'{min_out // 60}:{min_out % 60} hours before the start')
    elif -60 < min_out < 0:
        print(f'{abs(min_out)} minutes after the start')
    elif min_out <= -60:
        if min_out % 60 < -10:
            print(f'{abs(min_out) // 60}:0{min_out % 60} hours after the start')
        else:
            print(f'{abs(min_out) // 60}:{min_out % 60} hours after the start')



