def palindrome(word, index=0, words=[]):
    current_word = word
    if not current_word:
        words.append(current_word)
        return
    words.append(current_word)
    if current_word[index] == current_word[index - 1]:
        current_word = word[index + 1:index - 1]
        palindrome(current_word)

    if words[-1]:
        return f"{word} is not a palindrome"
    return f"{word} is a palindrome"


print(palindrome("abcba", 0))
print(palindrome("pertep", 0))