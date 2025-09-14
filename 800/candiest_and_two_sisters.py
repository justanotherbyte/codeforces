import math

cases = int(input())

def ways(n: int):
    mid = n / 2

    return math.ceil(n - (mid + 1))

for _ in range(cases):
    n = int(input())
    print(ways(n))
