import sys

sys.stdin = open('input.txt')

def blizard(N, arr, d_idx, s, x, y):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dx, dy = dir[d_idx]
    for i in range(1, s+1):
        nx, ny = x + i*dx, y + i*dy
        if 0<=nx<N and 0<=ny<N and arr[nx][ny]>0:
            arr[nx][ny] = 0

    return arr

def transform(N, arr, x, y):
    result = []
    cnt = 0
    base = 1
    base_cnt = 0
    dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    d_idx = 2
    for _ in range(1, N ** 2):
        dx, dy = dir[d_idx]
        x += dx
        y += dy
        result.append(arr[x][y])
        cnt += 1
        if cnt == base:
            cnt = 0
            d_idx += 1
            d_idx %= 4
            base_cnt += 1
            if base_cnt == 2:
                base += 1
                base_cnt = 0
    return result

def chain_boom(N, arr):
    q = []
    result = []
    cnt1, cnt2, cnt3 = 0, 0, 0
    while True:
        for x in arr:
            if not q:
                q.append(x)
                continue
            before = q[-1]
            if before==x:
                q.append(x)
            else:
                if len(q)>=4:
                    if q[-1]==1:
                        cnt1+= len(q)
                    elif q[-1]==2:
                        cnt2+= len(q)
                    elif q[-1]==3:
                        cnt3+= len(q)
                    q = []
                    q.append(x)
                else:
                    result.extend(q)
                    q = []
                    q.append(x)
        if q:
            if len(q)>=4:
                if q[-1] == 1:
                    cnt1 += len(q)
                elif q[-1] == 2:
                    cnt2 += len(q)
                elif q[-1] == 3:
                    cnt3 += len(q)
            else:
                result.extend(q)
            q=[]
        if len(arr)==len(result):
            break
        arr = result
        result = []
    return result, cnt1, cnt2, cnt3

def change(lst):
    q = []
    result = []
    for x in lst:
        if not q:
            q.append(x)
            continue
        before = q[-1]
        if before==x:
            q.append(x)
        else:
            result.append(len(q))
            result.append(q[-1])
            q = []
            q.append(x)

    if q:
        result.append(len(q))
        result.append(q[-1])
    return result

def inverse(N, lst):
    result = [[0] * N for _ in range(N)]
    cnt = 0
    base = 1
    base_cnt = 0
    dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    d_idx = 2
    x, y = N//2, N//2
    for i in range(min(len(lst), N**2-1)):
        dx, dy = dir[d_idx]
        x += dx
        y += dy
        result[x][y] = lst[i]
        cnt += 1
        if cnt == base:
            cnt = 0
            d_idx += 1
            d_idx %= 4
            base_cnt += 1
            if base_cnt == 2:
                base += 1
                base_cnt = 0
    return result

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dir_arr = [[0] * N for _ in range(N)]
start = (N//2, N//2)
x, y = start
cnt = 0
base = 1
base_cnt = 0
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
d_idx = 2
for _ in range(1, N**2):
    dx, dy = dir[d_idx]
    x+=dx
    y+=dy
    dir_arr[x][y] = (dx, dy)
    cnt+=1
    if cnt==base:
        cnt = 0
        d_idx += 1
        d_idx%=4
        base_cnt +=1
        if base_cnt==2:
            base += 1
            base_cnt=0
ans1, ans2, ans3 = 0, 0, 0

for _ in range(M):
    d, s = map(int, input().split())
    arr= blizard(N, arr, d-1, s, *start)
    lst = transform(N, arr, *start)
    lst = [x for x in lst if x]
    lst, r1, r2, r3 = chain_boom(N, lst)
    ans1 += r1
    ans2 += r2
    ans3 += r3
    lst = change(lst)
    arr = inverse(N, lst)
print(ans1 + ans2*2 + ans3*3)