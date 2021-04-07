from collections import deque


def bfs(i, j):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    q = deque()
    q.append((i, j, cnt))
    visit[i][j] = True
    max_cnt = 0
    while q:
        x, y, cnt = q.popleft()
        max_cnt = cnt
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and not visit[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visit[nx][ny] = True
    return max_cnt


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            distance = bfs(i, j)
            result = max(result, distance)

print(result)

