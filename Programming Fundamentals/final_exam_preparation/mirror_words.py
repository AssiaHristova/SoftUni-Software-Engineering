import re
text = input()

mirror_words = []
count = 0

pattern = r'(?P<separator>[\#\@])[a-zA-Z]{3,}(?P=separator){2}[a-zA-Z]{3,}(?P=separator)'

word_pairs = re.finditer(pattern, text)

word_pairs = [word.group() for word in word_pairs]

if len(word_pairs) == 0:
    print("No word pairs found!")
else:
    print(f"{len(word_pairs)} word pairs found!")

for word in word_pairs:
    word_1 = word[1:int(len(word) / 2) - 1]
    word_2 = word[int(len(word) / 2) + 1:-1]
    if word_1 == word_2[::-1]:
        mirror_word = word_1 + ' <=> ' + word_2
        mirror_words.append(mirror_word)

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))







