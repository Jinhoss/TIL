import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
infos = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    infos.append((r-1, c-1, m, s, d))

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for _ in range(K):
    while infos:
        r, c, m, s, d = infos.popleft()
        dr, dc = dir[d]
        nr = (r + dr * s)%N
        nc = (c + dc * s)%N
        arr[nr][nc].append((m, s, d))

    for i in range(N):
        for j in range(N):
            l = len(arr[i][j])
            if l > 1:
                sum_m, sum_s, cnt_odd, cnt_even = 0, 0, 0, 0
                while arr[i][j]:
                    m, s, d = arr[i][j].pop()
                    sum_m += m
                    sum_s += s
                    if d%2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                sum_m //= 5
                if not sum_m:
                    continue
                sum_s //= l
                if cnt_odd and cnt_even:
                    for idx in range(4):
                        infos.append((i, j, sum_m, sum_s, 2*idx + 1))
                else:
                    for idx in range(4):
                        infos.append((i, j, sum_m, sum_s, 2*idx))
            elif l == 1:
                infos.append((i, j, *arr[i][j].pop()))

print(sum([f[2] for f in infos]))





