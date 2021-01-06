flag = True

line = input()

if line == 'Monday':
    a = 1
elif line == 'Tuesday':
    a = 1
elif line == 'Wednesday':
    a = 1
    flag = False
elif line == 'Thursday':
    a = 1
elif line == 'Friday':
    a = 1

if flag:
    print('You have a meeting!')



