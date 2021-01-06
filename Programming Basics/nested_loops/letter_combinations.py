start_letter = input()
end_letter = input()
no_letter = input()

flag_1 = True
flag_2 = True
flag_3 = True
count = 0

for letter_1 in range(ord(start_letter), ord(end_letter) + 1):
    if letter_1 == ord(no_letter):
        flag_1 = False
    else:
        flag_1 = True
    for letter_2 in range(ord(start_letter), ord(end_letter) + 1):
        if letter_2 == ord(no_letter):
            flag_2 = False
        else:
            flag_2 = True
        for letter_3 in range(ord(start_letter), ord(end_letter) + 1):
            if letter_3 == ord(no_letter):
                flag_3 = False
            else:
                flag_3 = True
            if flag_1 and flag_2 and flag_3:
                count += 1
                print(f'{chr(letter_1)}{chr(letter_2)}{chr(letter_3)}', end=' ')
print(f'{count}')



