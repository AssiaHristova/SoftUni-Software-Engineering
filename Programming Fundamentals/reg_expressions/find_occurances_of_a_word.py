import re

sentence = input().lower()
word = input().lower()

pattern = r"\b" + word + r"\b"


occurrences = re.findall(pattern, sentence)

print(len(occurrences))



