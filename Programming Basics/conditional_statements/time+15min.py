hour = int(input())
minutes = int(input())

time_plus_15 = hour * 60 + minutes + 15

h = int(time_plus_15 / 60)
m = int(time_plus_15 % 60)

if h <= 23:
    H = h
else:
    H = (h - 24)

if m <= 59:
    M = m
else:
    M = (m - 59)

if M < 10:
    print(f'{H}:0{M}')
else:
    print(f'{H}:{M}')




