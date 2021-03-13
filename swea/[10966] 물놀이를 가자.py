# import sys
# sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    visit = [[0] * m for _ in range(n)]
    q = deque()
    result = 0
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    arr = []
    for i in range(n):
        lst = input()
        arr.append(lst)
        for j in range(m):
            if lst[j] == 'W':
                q.append((i, j))
    while q:
        x, y= q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and arr[nx][ny] == 'L':
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    result = 0
    for v in visit:
        result+=sum(v)
    print('#{} {}'.format(tc, result))
