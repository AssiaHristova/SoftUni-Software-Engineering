import re
text = input()

pattern = r"(^|(?<=\s))[a-z0-9]+\.?\-?\_?[a-z0-9]+@[a-z]+\-?[a-z]+\.[a-z]+\.?[a-z]+"

emails = re.finditer(pattern, text)

emails = [email.group() for email in emails]

print('\n'.join(emails))
