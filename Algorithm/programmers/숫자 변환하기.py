def solution(x, y, n):
    dp = [1e9] * (3*y + 1)
    dp[x] = 0
    for i in range(x, y):
        dp[i + n] = min(dp[i] + 1, dp[i + n])
        dp[i * 2] = min(dp[i] + 1, dp[i*2])
        dp[i*3] = min(dp[i] + 1, dp[i*3])
    if dp[y]>y:
        return -1
    return dp[y]