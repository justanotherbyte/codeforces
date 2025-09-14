# 141A
names = input() + input()
letters = list(input())

possible = True
for char in names:
    if char in letters:
        letters.remove(char)
    else:
        possible = False

r = possible and not letters
print("YES" if r else "NO")
