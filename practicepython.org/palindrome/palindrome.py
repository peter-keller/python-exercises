def palindrome(word):
    # function to check if a word is a palindrome or not
    return True if word == word[::-1] else False


print(palindrome("racecar"))