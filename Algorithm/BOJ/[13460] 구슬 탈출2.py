import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

def move(arr, x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy]!='#' and arr[x][y]!='O':
        x+=dx
        y+=dy
        cnt+=1

    return x, y, cnt


for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red = (i, j)
        if arr[i][j] == 'B':
            blue = (i, j)

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()
visit = {}
q.append((red, blue, 1))
min_cnt = 11
visit[(*red, *blue)]=1
while q:
    r, b, cnt= q.popleft()
    if cnt>10:
        continue
    for dx, dy in dir:
        rx, ry, rcnt = move(arr, *r, dx, dy)
        bx, by, bcnt = move(arr, *b, dx, dy)
        if arr[bx][by] == 'O':
            continue
        if arr[rx][ry] == 'O':
            if cnt<min_cnt:
                min_cnt = cnt
            break
        if (rx, ry) == (bx, by):
            if rcnt>bcnt:
                rx -= dx
                ry -= dy
            else:
                bx -= dx
                by -= dy
        if not visit.get((rx, ry, bx, by), 0):
            q.append(((rx, ry), (bx, by), cnt+1))
            visit[(rx, ry, bx, by)] = 1
if min_cnt<=10:
    print(min_cnt)
else:
    print(-1)
