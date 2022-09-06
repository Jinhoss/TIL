import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')

def calculate(arr, tx, ty, p_lst):
    d_lst = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    l = len(arr)
    visit = [[False] * l for _ in range(l)]
    q = []
    heapq.heappush(q, (0, tx, ty))
    visit[tx][ty] = True
    while q:
        d, x, y = heapq.heappop(q)
        if (x, y) in p_lst:
            return d, x, y
        for dx, dy in d_lst:
            nx, ny = x + dx, y + dy
            if 0<=nx<l and 0<=ny<l and not visit[nx][ny] and arr[nx][ny]==0:
                heapq.heappush(q, (d+1, nx, ny))
                visit[nx][ny] = True
    if not q:
        return -1

def calculate2(arr, tx, ty, px, py):
    d_lst = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    l = len(arr)
    visit = [[False] * l for _ in range(l)]
    q = deque()
    q.append((0, tx, ty))
    visit[tx][ty] = True
    while q:
        d, x, y = q.popleft()
        if (x, y) == (px, py):
            return d
        for dx, dy in d_lst:
            nx, ny = x + dx, y + dy
            if 0<=nx<l and 0<=ny<l and not visit[nx][ny] and arr[nx][ny]==0:
                q.append((d+1, nx, ny))
                visit[nx][ny] = True
    if not q:
        return -1

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tx, ty = list(map(int, input().split()))
tx, ty = tx -1, ty - 1
p_lst = []
target = {}
for idx in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    p_lst.append((x1-1, y1-1))
    target[(x1-1, y1-1)] = (x2-1, y2-1)
p_lst.sort(key=lambda x: (x[0], x[1]))
for _ in range(M):
    result = calculate(arr, tx, ty, p_lst)
    if result==-1:
        print(-1)
        break
    dist, px, py = result
    if dist > F:
        print(-1)
        break
    F -= dist
    p_lst = [x for x in p_lst if x != (px, py)]
    dist = calculate2(arr, px, py, *target[(px, py)])
    if dist > F or dist==-1:
        print(-1)
        break

    F += dist
    tx, ty = target[(px, py)]
else:
    print(F)





