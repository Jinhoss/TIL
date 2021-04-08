from bisect import bisect
n = int(input())
lst = list(map(int, input().split()))
dp = [lst[0]]
for i in range(1, n):
    if lst[i] > dp[-1]:
        dp.append(lst[i])
    else:
        dp[bisect(dp, lst[i])] = lst[i]
print(len(dp))

