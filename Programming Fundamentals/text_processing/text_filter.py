banned_words = input().split(', ')
text = input()

for ban_word in banned_words:
    text = text.replace(ban_word, '*' * len(ban_word))

print(text)