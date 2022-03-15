import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    rank = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]] += 1
    check = indegree[:]
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if check[a] < check[b]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
    q = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)
    result = 0
    result_lst = []
    if not q:
        result = 1
    while q:
        if len(q) > 1:
            result = 1
            break
        x = q.popleft()
        result_lst.append(x)
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            elif indegree[i] < 0:
                result = 1
                break
    if result or len(result_lst) < n:
        print('IMPOSSIBLE')
    else:
        print(*result_lst)
