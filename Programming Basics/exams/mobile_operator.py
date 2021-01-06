contract_time = input()
contract_type = input()
extra_net = input()
months = int(input())

sum_due = 0

if contract_time == 'one':
    if contract_type == 'Small':
        if extra_net == 'yes':
            sum_due = months * (9.98 + 5.50)
        else:
            sum_due = months * 9.98
    elif contract_type == 'Middle':
        if extra_net == 'yes':
            sum_due = months * (18.99 + 4.35)
        else:
            sum_due = months * 18.99
    elif contract_type == 'Large':
        if extra_net == 'yes':
            sum_due = months * (25.98 + 4.35)
        else:
            sum_due = months * 25.98
    else:
        if extra_net == 'yes':
            sum_due = months * (35.99 + 3.85)
        else:
            sum_due = months * 35.99
else:
    if contract_type == 'Small':
        if extra_net == 'yes':
            sum_due = (months * (8.58 + 5.50)) * 96.25 / 100
        else:
            sum_due = (months * 8.58) * 96.25 / 100
    elif contract_type == 'Middle':
        if extra_net == 'yes':
            sum_due = (months * (17.09 + 4.35)) * 96.25 / 100
        else:
            sum_due = (months * 17.09) * 96.25 / 100
    elif contract_type == 'Large':
        if extra_net == 'yes':
            sum_due = (months * (23.59 + 4.35)) * 96.25 / 100
        else:
            sum_due = (months * 23.59) * 96.25 / 100
    else:
        if extra_net == 'yes':
            sum_due = (months * (31.79 + 3.85)) * 96.25 / 100
        else:
            sum_due = (months * 31.79) * 96.25 / 100

print(f'{sum_due:.2f} lv.')
