from collections import deque
# import sys
# sys.stdin = open('input.txt')
# python은 시간초과, Pypy3로 제출

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dust = deque()
air_fresh = []
# 공기 청정기의 위치 탐색 첫 위치를 찾으면 바로 밑에 공기청정기가 한 개 더 있다.
for x in range(R):
    for y in range(C):
        if arr[x][y] == -1:
            air_fresh.append((x, y))
            air_fresh.append((x + 1, y))

# 미세먼지를 큐에 담아서 한 번에 확산시킨다.
for _ in range(T):
    for x in range(R):
        for y in range(C):
            if arr[x][y]>0:
                dust.append((x, y, arr[x][y]))
    # 배열에 존재하는 미세먼지의 수만큼 반복
    while dust:
        x, y, A = dust.popleft()
        cnt = 0
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                arr[nx][ny] += A//5
                arr[x][y] -= A//5

    arr2 = [lst[:] for lst in arr]
    # 공기청정기 위치에 따라 먼지를 이동시켜 줌
    for x in range(R):
        for y in range(C):
            if x == air_fresh[0][0] and air_fresh[0][1] <y < C:
                arr[x][y] = arr2[x][y-1]
            elif y == C - 1 and x < air_fresh[0][0]:
                arr[x][y] = arr2[x + 1][y]
            elif x == 0 and y < C:
                arr[x][y] = arr2[x][y + 1]
            elif y == 0 and x < air_fresh[0][0]:
                arr[x][y] = arr2[x - 1][y]
            elif  x == air_fresh[1][0] and air_fresh[1][1] < y < C:
                arr[x][y] = arr2[x][y-1]
            elif y == C - 1 and x > air_fresh[1][0]:
                arr[x][y] = arr2[x - 1][y]
            elif x == R - 1 and y < C - 1:
                arr[x][y] = arr2[x][y + 1]
            elif y == 0 and x > air_fresh[1][0]:
                arr[x][y] = arr2[x + 1][y]
    # 공기청정기가 이동하는 것을 방지
    arr[air_fresh[0][0]][air_fresh[0][1] + 1] = 0
    arr[air_fresh[1][0]][air_fresh[1][1] + 1] = 0
sum_dust = 0
for x in range(R):
    for y in range(C):
        if arr[x][y]:
            sum_dust+=arr[x][y]
# 공기청정기 두 개가 있으므로 +2
print(sum_dust + 2)