def add(pieces, piece, composer, key):
    if piece in pieces:
        print(f"{piece} is already in the collection!")
    else:
        pieces[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove(pieces, piece):
    if piece in pieces:
        pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(pieces, piece, new_key):
    if piece in pieces:
        pieces[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


n = int(input())

pieces = {}

for i in range(n):
    line = input().split("|")
    for ele in line:
        piece, composer, key = line[::]
        pieces[piece] = [composer, key]

text = input()

while not text == "Stop":
    command = text.split("|")
    if command[0] == 'Add':
        piece, composer, key = command[1:]
        add(pieces, piece, composer, key)
    elif command[0] == 'Remove':
        piece = command[1]
        remove(pieces, piece)
    elif command[0] == 'ChangeKey':
        piece, key = command[1:]
        change_key(pieces, piece, key)

    text = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1][0]))

for piece in sorted_pieces:
    print(f"{piece[0]} -> Composer: {piece[1][0]}, Key: {piece[1][1]}")
