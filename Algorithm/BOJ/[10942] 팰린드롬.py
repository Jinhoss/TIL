import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if lst[i] == lst[j]:
            if j - i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i + 1][j - 1]

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
