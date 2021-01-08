string = input()
n = int(input())


def repeat_string(text, num):
    for i in range(num):
        print(text, end='')


repeat_string(string, n)

