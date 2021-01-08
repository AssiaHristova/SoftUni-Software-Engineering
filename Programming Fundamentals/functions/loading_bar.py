def loading_bar(num):
    loading_list = []
    if num % 10 == 0:
        for symbol_1 in range(int(num / 10)):
            loading_list.append('%')
        for symbol_2 in range(len(loading_list), 10):
            loading_list.append('.')
    loading_string = ''.join(loading_list)
    if num == 100:
        print('100% Complete!')
        print(f'[{loading_string}]')
    else:
        print(f'{num}% [{loading_string}]')
        print('Still loading...')


integer = int(input())
loading_bar(integer)
