text = input()

vowels = ['a', 'e', 'i', 'o', 'u']
vowels += [char.upper for char in vowels]

no_vowels = [char for char in text if char not in vowels]

print(''.join(no_vowels))

