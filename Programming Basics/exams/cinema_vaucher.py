voucher = int(input())
purchase = input()

count_tickets = 0
count_others = 0
price = 0

while purchase != "End":
    if len(purchase) > 8:
        count_1 = 0
        for letter in purchase:
            symbol = ord(letter)
            count_1 += 1
            price += symbol
            if count_1 == 2:
                break
        if price < voucher:
            count_tickets += 1
    else:
        count_2 = 0
        for letter in purchase:
            symbol = ord(letter)
            count_2 += 1
            price += symbol
            if count_2 == 1:
                break
        if price < voucher:
            count_others += 1
    if price >= voucher:
        break

    purchase = input()

print(f"{count_tickets}")
print(f"{count_others}")

