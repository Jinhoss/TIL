from collections import deque
import sys

input = sys.stdin.readline

def bfs(mid):
    visit[s] = True
    q = deque()
    q.append(s)
    while q:
        start = q.popleft()
        if start == e:
            return True
        for next, cost in lst[start]:
            if not visit[next] and mid <= cost:
                q.append(next)
                visit[next] = True
    return False


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])

s, e = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
    visit = [False] * (N + 1)
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)