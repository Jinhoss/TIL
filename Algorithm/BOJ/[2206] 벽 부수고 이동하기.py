from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
q = deque()
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visit[0][0][1] = 0
q.append((0, 0, 1))
result = False
while q:
    x, y, check= q.popleft()
    if x == N - 1 and y == M - 1:
        print(visit[x][y][check] + 1)
        result = True
        break
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][check] and arr[nx][ny] == '0':
            visit[nx][ny][check] = visit[x][y][check] + 1
            q.append((nx, ny, check))
        elif 0 <= nx < N and 0 <= ny < M and check and not visit[nx][ny][0] and arr[nx][ny] == '1':
            visit[nx][ny][0] = visit[x][y][check] + 1
            q.append((nx, ny, 0))
if not result:
    print(-1)