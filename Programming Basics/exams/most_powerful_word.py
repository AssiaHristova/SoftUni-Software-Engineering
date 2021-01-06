import math
import sys

word = input()
max_sum = -sys.maxsize
max_word = ''

while word != "End of words":
    sum_letters = 0
    count = 0
    for letter in word:
        number = ord(letter)
        sum_letters += number
    for letter in word:
        count += 1
        length = len(word)
        if count == 1:
            if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter =='U' or letter == 'y' or letter == 'Y':
                sum_letters = sum_letters * length
            else:
                sum_letters = math.floor(sum_letters / length)
    if sum_letters > max_sum:
        max_sum = sum_letters
        max_word = word

    word = input()


print(f"The most powerful word is {max_word} - {max_sum}")



