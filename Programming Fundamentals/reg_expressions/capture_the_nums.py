import re
data = input()

data_all = ''

while not data == '':
    data_all += data
    data = input()

pattern = r'\d+'

nums = re.findall(pattern, data_all)

print(*nums)


