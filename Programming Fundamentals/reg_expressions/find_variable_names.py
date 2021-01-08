import re
data = input()

pattern = r'(?<=\b_)[A-Za-z0-9]+\b'

var_names = re.findall(pattern, data)

print(','.join(var_names))

