from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i]

    while q:
        x = q.popleft()
        for nx in graph[x]:
            indegree[nx] -= 1
            dp[nx] = max(dp[x] + times[nx], dp[nx])
            if indegree[nx] == 0:
                q.append(nx)
    w = int(input())
    print(dp[w])
