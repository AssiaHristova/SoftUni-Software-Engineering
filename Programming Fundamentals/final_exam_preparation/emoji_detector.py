import re
text = input()

cool_threshold = 1

pattern = r'(?P<separator>[\:\*]){2}[A-Z][a-z][a-z]+(?P=separator){2}'

matches = re.finditer(pattern, text)
emojis = [match.group() for match in matches]

for el in text:
    if el.isdigit():
        cool_threshold *= int(el)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')

for emoji in emojis:
    coolness = 0
    for symbol in emoji:
        if symbol.isalpha():
            coolness += ord(symbol)
    if coolness >= cool_threshold:
        print(f'{emoji}')

