import math

hours_need = int(input())
days = int(input())
extra_workers = int(input())

days_have = days * (90 / 100)
hours_have = days_have * 8
extra_hours = extra_workers * 2 * days
hours_total = hours_have + extra_hours

if hours_total >= hours_need:
    print(f'Yes!{math.floor(hours_total) - hours_need} hours left.')
else:
    print(f'Not enough time!{hours_need - math.floor(hours_total)} hours needed.')