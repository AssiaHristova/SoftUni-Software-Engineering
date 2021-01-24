def balanced_parentheses(text, symbol_1, symbol_2):
    is_balanced = False
    for i in range(len(text)):
        if text[i] == symbol_1 and text[-i - 1] == symbol_2:
            is_balanced = True
    return is_balanced


def balanced_intervals(text):
    is_balanced = True
    for i in range(len(text)):
        if text[i] == ' ':
            if not text[-i - 1] == ' ':
                is_balanced = False
    return is_balanced


line = input()

parentheses_1 = balanced_parentheses(line, '(', ')')
parentheses_2 = balanced_parentheses(line, '{', '}')
parentheses_3 = balanced_parentheses(line, '[', ']')
intervals = balanced_intervals(line)

if parentheses_1 and parentheses_2 and parentheses_3 and intervals:
    print('YES')
else:
    print('NO')
