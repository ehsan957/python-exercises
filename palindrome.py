def isPalndrome(word):
    word = word.lower()
    length = len(word)
    for i in range(length//2):
        if word[i] != word[-1-i]:
            return False
    return True


print(isPalndrome("kayuk"))