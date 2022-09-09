import sys

sys.stdin = open('input.txt')

def move(N, cloud, d_idx, cnt):
    dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    dx, dy = dir[d_idx]
    result = []
    for x, y in cloud:
        nx = x + dx*cnt
        ny = y + dy*cnt
        nx%=N
        ny%=N
        result.append((nx, ny))
    return result

def rain(arr, cloud):
    for x, y in cloud:
        arr[x][y] += 1

    return arr

def water_copy(N, arr, cloud):
    dir = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    for x, y in cloud:
        water = 0
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]>0:
                water+=1

        arr[x][y] += water
    return arr

def make_cloud(N, arr, cloud):
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and (i, j) not in cloud:
                arr[i][j]-=2
                result.append((i, j))

    return arr, result

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    d, s = map(int, input().split())
    cloud = move(N, cloud, d-1, s)
    arr = rain(arr, cloud)
    arr = water_copy(N, arr, cloud)
    arr, cloud = make_cloud(N, arr, cloud)

ans = 0
for lst in arr:
    ans += sum(lst)

print(ans)
