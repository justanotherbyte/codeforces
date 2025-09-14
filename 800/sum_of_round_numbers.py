# 1352A

n = int(input())

for _ in range(n):
    num = int(input())

    summands = []
    mul = 1

    while num > 0:
        r = num % 10
        if r != 0:
            summands.append(r * mul)
        mul *= 10
        num -= r
        num //= 10

    print(len(summands))
    print(" ".join(str(s) for s in summands))
