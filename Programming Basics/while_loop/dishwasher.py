bottles = int(input())
command = input()

count = 0
plates = 0
pots = 0
detergent_need = 0

while command != 'End':
    dishes = int(command)
    count += 1
    if count % 3 != 0:
        plates += dishes
        detergent_need += dishes * 5
    else:
        detergent_need += dishes * 15
        pots += dishes
    if detergent_need >= bottles * 750:
        break

    command = input()

if detergent_need >= bottles * 750:
    print(f'Not enough detergent, {detergent_need - (bottles * 750)} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {(bottles * 750) - detergent_need} ml.')
