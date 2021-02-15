try:
    text = input()
    n = int(input())

    for i in range(n):
        print(text, end='')

except ValueError:
    print("Variable times must be an integer")



