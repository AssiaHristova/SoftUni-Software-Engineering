save_sum = 0
save_amount = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while save_sum < budget:
        save_amount = float(input())
        save_sum += save_amount
        if save_sum >= budget:
            save_sum = 0
            print(f'Going to {destination}!')
            break
