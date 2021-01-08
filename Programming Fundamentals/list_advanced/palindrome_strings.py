words = input().split()
searched_word = input()

palindromes = [word for word in words if word == word[::-1]]
count = palindromes.count(searched_word)

print(palindromes)
print(f"Found palindrome {count} times")



