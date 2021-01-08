tickets = input().split(', ')


for ticket in tickets:
    count = 0
    ticket = ticket.strip()
    if len(ticket) == 20:
        left_half = ticket[:10]
        right_half = ticket[10:]
        winning_symbols = ['@', '#', '$', '^']
        for winning_symbol in winning_symbols:
            if winning_symbol * 6 in right_half and winning_symbol * 6 in left_half:
                count_left = 6
                count_right = 6
                for i in range(7, 11):
                    if winning_symbol * i in left_half:
                        count_left = i
                    if winning_symbol * i in right_half:
                        count_right = i
                count = min(count_left, count_right)
                if count_left == 10 and count_right == 10:
                    print(f'ticket "{ticket}" - {count_right}{winning_symbol} Jackpot!')
                else:
                    print(f'ticket "{ticket}" - {count}{winning_symbol}')
            else:
                count += 1
                if count == 4:
                    print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")






