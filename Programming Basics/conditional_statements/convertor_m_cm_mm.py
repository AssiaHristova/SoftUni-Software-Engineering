distance = float(input())
measure = input()
result_measure = input()

if measure == 'm' and result_measure == 'cm':
    print(f'{distance * 100:.3f}')
elif measure == 'm' and result_measure == 'mm':
    print(f'{distance * 1000:.3f}')
elif measure == 'cm' and result_measure == 'mm':
    print(f'{distance * 10:.3f}')
elif measure == 'cm' and result_measure == 'm':
    print(f'{distance / 100:.3f}')
elif measure == 'mm' and result_measure == 'cm':
    print(f'{distance / 10:.3f}')
elif measure == 'mm' and result_measure == 'm':
    print(f'{distance / 1000:.3f}')




