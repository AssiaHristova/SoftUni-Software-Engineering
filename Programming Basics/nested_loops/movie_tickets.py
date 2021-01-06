count_student = 0
count_standard = 0
count_kid = 0
total_count = 0


while True:
    movie = input()
    if movie == 'Finish':
        print(f'Total tickets: {total_count}')
        print(f'{(count_student / total_count) * 100:.2f}% student tickets.')
        print(f'{count_standard / total_count * 100:.2f}% standard tickets.')
        print(f'{count_kid / total_count * 100:.2f}% kids tickets.')
        break
    free_seats = int(input())
    ticket_count = 0
    while ticket_count < free_seats:
        ticket = input()
        if ticket == 'student':
            count_student += 1
            ticket_count += 1
        elif ticket == 'standard':
            count_standard += 1
            ticket_count += 1
        elif ticket == 'kid':
            count_kid += 1
            ticket_count += 1
        elif ticket == 'End':
            break

        total_count = count_student + count_standard + count_kid
    print(f'{movie} - {(ticket_count / free_seats) * 100:.2f}% full.')






