def replace_chars(lines, chars):
    result = []
    for line in even_lines:
        for char in line:
            if char in special_chars:
                line = line.replace(char, "@")
        result.append(line)
    return result


with open('text.txt', 'w') as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n-Quick, hide here. It is safer.")

with open('text.txt', 'r') as file:
    lines = file.readlines()
    even_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
    special_chars = ["-", ",", ".", "!", "?"]
    result = replace_chars(even_lines, special_chars)
    for line in result:
        line = line.split()[::-1]
        print(*line)



