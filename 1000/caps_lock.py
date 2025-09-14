# 131A
word = input()

if word[0].lower() == word[0] and word[1:] == word[1:].upper():
    print(word.title())
elif word.upper() == word:
    print(word.lower())
else:
    print(word)