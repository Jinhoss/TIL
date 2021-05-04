from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    cnt, *lst = map(int, input().split())
    for i in range(cnt - 1):
        graph[lst[i]].append(lst[i + 1])
        indegree[lst[i + 1]] += 1
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
result = []
while q:
    x = q.popleft()
    result.append(x)

    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

if len(result) == N:
    for x in result:
        print(x)
else:
    print(0)