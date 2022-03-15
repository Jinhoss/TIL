import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
t = []
p = []
max_value = 0
for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
for i in range(N - 1, -1, -1):
    time = t[i] + i
    if time <= N:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)