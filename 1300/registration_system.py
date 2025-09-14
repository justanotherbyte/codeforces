# 4C
n = int(input())

names = [input() for _ in range(n)]

db: dict[str, int] = {}

for name in names:
    if name not in db:
        print("OK")
        db[name] = 1
    else:
        num = db[name]
        print(f"{name}{num}")
        db[name] = num + 1
