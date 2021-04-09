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
ans = []
l = len(dp)
print(l)
for idx in range(n - 1, -1, -1):
    if idx_lst[idx] == l - 1:
        ans.append(lst[idx])
        l -= 1
print(*ans[::-1])