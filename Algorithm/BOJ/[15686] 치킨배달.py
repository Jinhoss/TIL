import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def cal_d(arr, chicken_lst, house_lst):
    chick_d = 0
    for hx, hy in house_lst:
        min_d = 1e9
        for x, y in chicken_lst:
            d = abs(x-hx) + abs(y - hy)
            if d<min_d:
                min_d = d
        chick_d += min_d
    return chick_d


chicken_lst = []
house_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken_lst.append((i, j))
        elif arr[i][j] == 1:
            house_lst.append((i, j))

q = deque()
q.append((0, []))
min_d = 1e9
while q:
    idx, lst = q.popleft()
    if len(lst) == M:
        d = cal_d(arr, lst, house_lst)
        if d<min_d:
            min_d = d
        continue
    if idx >=len(chicken_lst):
        continue
    lst2 = [x for x in lst]
    lst3 = [x for x in lst]
    q.append((idx+1, lst2))
    c = chicken_lst[idx]
    q.append((idx+1, lst3 + [c]))

print(min_d)