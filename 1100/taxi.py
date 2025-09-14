# 158B
_ = int(input())

groups = list(map(int, input().split(" ")))
groups.sort(reverse=True)

num = 0
car = 0
remaining = sum(groups)

counts = {}
for idx, n in enumerate(groups):
    if n not in counts:
        counts[n] = 1
    else:
        counts[n] += 1

while remaining > 0:
    s = groups.pop(0)
    car = s

    diff = 4 - car
    for d in range(diff, 0, -1):
        if d not in counts:
            continue
        
        while counts[d] > 0:
            if car + d <= 4:
                counts[d] -= 1
                car += d
            else:
                break

    num += 1
    remaining -= car

print(num)