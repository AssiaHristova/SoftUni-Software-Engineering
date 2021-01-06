last_sector = input()
rows_sector_A = int(input())
seats_odd_row = int(input())

seats_odd = 0
seats_even = 0

for sector in range(1, (ord(last_sector) - 64) + 1):
    if sector > 1:
        rows_sector_A += 1
    for row in range(1, rows_sector_A + 1):
        if row % 2 != 0:
            for seat_odd_row in range(1, seats_odd_row + 1):
                seats_odd += 1
                print(f'{chr(sector + 64)}{row}{chr(seat_odd_row + 96)}')
        else:
            for seat_even_row in range(1, (seats_odd_row + 2) + 1):
                seats_even += 1
                print(f'{chr(sector + 64)}{row}{chr(seat_even_row + 96)}')
print(f'{seats_odd + seats_even}')

