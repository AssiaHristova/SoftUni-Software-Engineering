def custom_split(text, sep):
    result = text.split(sep)
    return result


print(custom_split('Hello,there', ','))
print(custom_split('How are you', ' '))
print(custom_split('blue,red,green', ','))

