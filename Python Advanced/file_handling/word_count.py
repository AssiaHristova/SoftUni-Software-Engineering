import re


def create_files():
    with open('words.txt', 'w') as file:
        file.write('quick is fault')

    with open('text.txt', 'w') as file:
        file.write("-I was quick to judge him, but it wasn't his fault.-Is this some kind of joke?! Is it?-Quick, hide here…It is safer.")


def get_file_words(path_to_file):
    with open(path_to_file, 'r') as file:
        text = ''.join(file.readlines())
        words = re.findall(r"[a-z']+", text.lower())
        return words


def write_result(result):
    with open('output.txt', 'w') as file:
        file.writelines('\n'.join(result))


match_words = {}
create_files()
words_file = get_file_words('words.txt')
text_file = get_file_words('text.txt')

for word in words_file:
    if word in text_file:
        match_words[word] = text_file.count(word)

sorted_match_words = sorted(match_words.items(), key=lambda x:x[1], reverse=True)

result = [f'{el[0]} - {el[1]}' for el in sorted_match_words]

write_result(result)







