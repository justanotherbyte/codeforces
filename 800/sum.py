n = int(input())

for _ in range(n):
    nums = list(map(int, input().split(" ")))
    m = max(nums)
    nums.remove(m)

    if sum(nums) == m:
        print("YES")
    else:
        print("NO")
