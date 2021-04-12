import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cctv_lst = []
cctv5_lst = []
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = N * M
for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 4:
            cctv_lst.append((i, j, matrix[i][j]))
            result -= 1
        elif matrix[i][j] == 5:
            cctv5_lst.append((i, j))
            result -= 1
        elif matrix[i][j] == 6:
            result -= 1
while cctv5_lst:
    x, y = cctv5_lst.pop()
    for dx, dy in delta:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if not 0 <= nx < N or not 0 <= ny < M or matrix[nx][ny] == 6:
                break
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = -1
                result -=1

l = len(cctv_lst)
stack = []
stack.append((0, result, matrix))

while stack:
    idx, cnt, arr = stack.pop()
    if idx == l:
        if cnt < result:
            result = cnt
        continue
    x, y, cctv = cctv_lst[idx]
    if cctv == 1:
        for dx, dy in delta:
            arr2 = [lst[:] for lst in arr]
            minus = 0
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if not 0 <= nx < N or not 0 <= ny < M or arr2[nx][ny] == 6:
                    break
                if arr2[nx][ny] == 0:
                    arr2[nx][ny] = -1
                    minus += 1
            stack.append((idx + 1, cnt - minus, arr2))
    elif cctv == 2:
        for move in [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]]:
            arr2 = [lst[:] for lst in arr]
            minus = 0
            for dx, dy in move:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not 0 <= nx < N or not 0 <= ny < M or arr2[nx][ny] == 6:
                        break
                    if arr2[nx][ny] == 0:
                        arr2[nx][ny] = -1
                        minus += 1
            stack.append((idx + 1, cnt - minus, arr2))
    elif cctv == 3:
        for move in [[(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]:
            arr2 = [lst[:] for lst in arr]
            minus = 0
            for dx, dy in move:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not 0 <= nx < N or not 0 <= ny < M or arr2[nx][ny] == 6:
                        break
                    if arr2[nx][ny] == 0:
                        arr2[nx][ny] = -1
                        minus += 1
            stack.append((idx + 1, cnt - minus, arr2))

    elif cctv == 4:
        for move in [[(1, 0), (-1, 0), (0, 1)], [(1, 0), (-1, 0), (0, -1)], [(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)]]:
            arr2 = [lst[:] for lst in arr]
            minus = 0
            for dx, dy in move:
                nx, ny = x, y
                while True:
                    nx += dx
                    ny += dy
                    if not 0 <= nx < N or not 0 <= ny < M or arr2[nx][ny] == 6:
                        break
                    if arr2[nx][ny] == 0:
                        arr2[nx][ny] = -1
                        minus += 1
            stack.append((idx + 1, cnt - minus, arr2))
print(result)


