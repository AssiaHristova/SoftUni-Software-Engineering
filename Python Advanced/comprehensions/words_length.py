strings = {string: len(string) for string in input().split(', ')}

strings_list = [f'{string} -> {length}' for string, length in strings.items()]

print(', '.join(strings_list))









