N = int(input())

points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
others = 0
black_balls = 0

for i in range(1, N + 1):
    color = input()
    if color == 'red':
       points += 5
       red_balls += 1
    elif color == 'orange':
        points += 10
        orange_balls +=1
    elif color == 'yellow':
        points += 15
        yellow_balls += 1
    elif color == 'white':
        points += 20
        white_balls += 1
    elif color == 'black':
        points = points / 2
        black_balls += 1
    else:
        others += 1

print(f'Total points: {points}')
print(f'Points from red balls: {red_balls}')
print(f'Points from orange balls: {orange_balls}')
print(f'Points from yellow balls: {yellow_balls}')
print(f'Points from white balls: {white_balls}')
print(f'Other colors picked: {others}')
print(f'Divides from black balls: {black_balls}')






