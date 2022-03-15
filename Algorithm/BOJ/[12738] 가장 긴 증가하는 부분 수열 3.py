from bisect import bisect_left

input()
lst = list(map(int, input().split()))
dp = []
for x in lst:
    idx = bisect_left(dp, x)
    if len(dp) <= idx:
        dp.append(x)
    else:
        dp[idx] = x
print(len(dp))
print(*dp)