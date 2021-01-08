string = input().split('>')

strength = 0
strength_left = 0

for word in string:
    if len(word) > 0:
        if word[0].isdigit():
            strength = int(word[0]) + strength_left
            strength_left = 0
            if word == string[-1]:
                for j in range(strength):
                    if strength > len(word):
                        strength_left += 1
                        strength -= 1
                    else:
                        word = word[1:]
                        strength -= 1
            else:
                for j in range(strength):
                    if strength > len(word):
                        strength_left += 1
                        strength -= 1
                    else:
                        word = word[1:]
                        strength -= 1
                word += '>'
        else:
            word += '>'
        print(word, end='')




