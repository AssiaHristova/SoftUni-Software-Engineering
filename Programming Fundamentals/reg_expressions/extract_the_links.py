import re
data = input()

data_all = ''

while not data == '':
    data_all += (data + ' ')
    data = input()

pattern = r'(^|(?<=\s))www\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))'

links = re.finditer(pattern, data_all)

links = [link.group() for link in links]

print('\n'.join(links))







