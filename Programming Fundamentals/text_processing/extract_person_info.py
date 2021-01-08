import re

N = int(input())

pattern = r'(?<=@)(?P<name>.+)(?=\|).+(?<=#)(?P<age>.+)(?=\*)'

for _ in range(N):
    line = input()
    data = re.finditer(pattern, line)
    for el in data:
        a = el.groupdict()
        print(f"{a['name']} is {a['age']} years old.")
