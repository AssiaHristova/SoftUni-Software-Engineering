import re

n = int(input())

pattern = r'^(?P<separator>[$|%])(?P<tag>[A-Z][a-z]{2,})(?P=separator)\:\s\[(?P<group_1>[0-9]+)\]\|\[(?P<group_2>[0-9]+)\]\|\[(?P<group_3>[0-9]+)\]\|$'

for _ in range(n):
    line = input()
    decrypted_message = ''
    new_ele = ''
    is_valid = re.search(pattern, line)
    message = re.finditer(pattern, line)
    if is_valid is not None:
        for el in message:
            p = el.groupdict()
            tag = p['tag']
            group_1 = p['group_1']
            group_2 = p['group_2']
            group_3 = p['group_3']
            decrypted_message = chr(int(group_1)) + chr(int(group_2)) + chr(int(group_3))
            print(f"{tag}: {decrypted_message}")
    else:
        print('Valid message not found!')



