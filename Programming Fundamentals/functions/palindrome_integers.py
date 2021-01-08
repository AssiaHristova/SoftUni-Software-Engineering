string = input()


def palindrome_integers(num):
    result = []
    list_nums = num.split(', ')
    for symbol in list_nums:
        if str(symbol) == str(symbol[::-1]):
            result.append(str(True))
        else:
            result.append(str(False))
    result_as_string = '\n'.join(result)
    return result_as_string


print(palindrome_integers(string))

