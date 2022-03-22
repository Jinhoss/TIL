from collections import deque
#
N, M = map(int, input().split())


q = deque()
q.append((0, N))
limit = 100001
visit = [False] * limit
result = {}

while q:
    time, cur = q.popleft()
    nx_lst = [cur + 1, cur - 1, cur * 2]
    if cur == M:
        result[time] = result.get(time, 0) + 1
    else:
        visit[cur] = True
        for nx in nx_lst:
            if 0 <= nx < limit and not visit[nx]:
                q.append((time + 1, nx))

x = sorted(result.items())
print(x[0][0])
print(x[0][1])
