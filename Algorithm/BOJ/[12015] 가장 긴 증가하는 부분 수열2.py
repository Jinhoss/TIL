from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))
dp = []
idx_lst = []
for i in range(n):
    idx = bisect_left(dp, lst[i])
    if len(dp) <= idx:
        dp.append(lst[i])
        idx_lst.append(len(dp) - 1)
    else:
        dp[idx] = lst[i]
        idx_lst.append(idx)
l = len(dp)
print(l)