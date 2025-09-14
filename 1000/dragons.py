# 230A

health, n = list(map(int, input().split(" ")))

pairs = []

for _ in range(n):
    dragon, bonus = list(map(int, input().split(" ")))
    pairs.append((dragon, bonus))

pairs.sort(key=lambda x: x[0])

for dragon, bonus in pairs:
    if health > dragon:
        health += bonus
    else:
        print("NO")
        break
else:
    print("YES")