import sys
input = sys.stdin.readline
from collections import deque


def magic(matrix, x, y, L):
    matrix2 = [[matrix[i][j] for j in range(y, y+L)] for i in range(x, x + L)]
    ret = [[0] * L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            ret[j][L-1-i] = matrix2[i][j]

    return ret




N, Q = map(int, input().split())
size = 2**N
arr = [list(map(int, input().split())) for _ in range(size)]
step_lst = list(map(int, input().split()))
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for step in step_lst:
    L = 2**step
    r = size//L
    for i in range(r):
        for j in range(r):
            x = i * L
            y = j * L
            result = magic(arr, x, y, L)
            for ci in range(L):
                for cj in range(L):
                    arr[x+ci][y+cj] = result[ci][cj]
    ret = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if not arr[i][j]:
                ret[i][j] = arr[i][j]
                continue
            cnt = 0
            for dx, dy in dir:
                nx, ny = i + dx, j + dy
                if 0<=nx<size and 0<=ny<size and arr[nx][ny]>0:
                    cnt += 1
            if cnt >=3:
                ret[i][j] = arr[i][j]
            else:
                ret[i][j] = arr[i][j] - 1
    arr = ret

sum_ice = 0
visit = [[False] * size for _ in range(size)]
max_size = 0
for i in range(size):
    for j in range(size):
        amount = arr[i][j]
        sum_ice += amount
        if amount and not visit[i][j]:
            q = deque()
            q.append((i, j))
            visit[i][j] = True
            cnt = 0
            while q:
                cx, cy = q.popleft()
                cnt += 1
                for dx, dy in dir:
                    nx, ny = cx + dx, cy + dy
                    if 0<=nx<size and 0<=ny<size and arr[nx][ny] and not visit[nx][ny]:
                        visit[nx][ny] = True
                        q.append((nx, ny))

            if cnt > max_size:
                max_size = cnt
print(sum_ice)
print(max_size)



