book_to_find = input()
book = input()

count = 0

while book != 'No More Books':
    if book == book_to_find:
        break
    count += 1

    book = input()

if book == book_to_find:
    print(f'You checked {count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {count} books.')
