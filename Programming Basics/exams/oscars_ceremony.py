rent = int(input())

statuettes = rent * 0.70
catering = statuettes * 0.85
sound = catering / 2

cost = rent + statuettes + catering + sound

print(f'{cost:.2f}')

