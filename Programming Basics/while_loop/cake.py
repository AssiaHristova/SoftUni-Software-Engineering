width = int(input())
length = int(input())
command = input()

size = width * length
cakes_all = 0
cakes_out = 0

while command != 'STOP':
    cakes = int(command)
    cakes_all += cakes
    cakes_out = size - cakes_all
    if cakes_out <= 0:
        break

    command = input()

if cakes_out <= 0:
    print(f'No more cake left! You need {abs(cakes_out)} pieces more.')
else:
    print(f'{cakes_out} pieces are left.')