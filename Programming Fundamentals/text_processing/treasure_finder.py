import re

key = input().split()

pattern = r'(?<=&)(?P<treasure>.+)(?=&).+(?<=<)(?P<coordinates>.+)(?=>)'

line = input()

while not line == "find":
    message = ''
    while len(key) < len(line):
        key += key
    for i in range(len(line)):
        k = ord(line[i]) - int(key[i])
        message += chr(k)
    result = re.finditer(pattern, message)
    for el in result:
        p = el.groupdict()
        print(f"Found {p['treasure']} at {p['coordinates']}")

    line = input()