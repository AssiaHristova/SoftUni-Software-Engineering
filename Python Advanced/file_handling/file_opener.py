try:
    with open('text_file.txt', 'r') as file:
        print('File found')
except FileNotFoundError:
    print('File not found')