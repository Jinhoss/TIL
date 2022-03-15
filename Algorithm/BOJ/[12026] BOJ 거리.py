import sys
input = sys.stdin.readline

# 처음에 무조건 가까운 문자로 이동하는 형태로 구현하였으나
# 각 문자의 거리에 따라 적당한 거리를 이동하는 것이 더 작은 값이 나오는 케이스가 존재
# DP로 구현
N = int(input())
lst = input()
dp = [float('inf')] * N
before = {'B':'J', 'O':'B', 'J':'O'}
dp[0] = 0
for i in range(1, N):
    # 현재 문자의 위치에 따라 이전에 들를 수 있는 값들을 돌며 최소값을 저장
    before_v = before[lst[i]]
    for before_i in range(i):
        if lst[before_i] == before_v:
            dp[i] = min(dp[i], dp[before_i] + (i - before_i) ** 2)
# 마지막에 도달했다면 그 값이 계산되어 무한대가 아닌 값으로 저장되어 있을 것
if dp[N-1] < float('inf'):
    print(dp[N - 1])
else:
    print(-1)