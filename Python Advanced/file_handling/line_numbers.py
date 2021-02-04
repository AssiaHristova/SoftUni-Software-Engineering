import re


def letter_counter(line):
    letter_count = 0
    words = re.findall(r"[a-zA-Z]+", line)
    for word in words:
        letter_count += len(word)
    return letter_count


def punctuation_marks_counter(line):
    punctuation_count = 0
    punctuation_marks = ["-", ",", ".", "!", "?", "'"]
    for char in line:
        if char in punctuation_marks:
            punctuation_count += 1
    return punctuation_count


def write_result(result):
    with open('output.txt', 'w') as file:
        file.writelines('\n'.join(result))



with open('text.txt', 'r') as file:
    lines = file.readlines()
    counter_lines = []
    for line in lines:
        letter_count = letter_counter(line)
        punctuation_count = punctuation_marks_counter(line)
        line = line.replace('\n', '')
        line += f'({letter_count})({punctuation_count})'
        counter_lines.append(line)

    numerated_lines = [f'Line {i + 1}: ' + counter_lines[i] for i in range(len(counter_lines))]
    write_result(numerated_lines)
    


