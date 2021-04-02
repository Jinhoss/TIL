from collections import deque
# import sys
# sys.stdin = open('input.txt')

N, M, x, y, num = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 처음엔 모든 면이 0
dice = [0] * 6

# 바닥, 좌, 위, 우, 앞, 뒤
# 오른쪽으로 굴림 -> 앞, 뒤 고정
# 위 -> 우, 좌-> 위, 우->바닥, 바닥->좌
# 왼쪽은 오른쪽 반대
# 위로 굴림 ->좌, 우 고정
# 바닥 -> 앞, 위 -> 뒤, 앞-> 위, 뒤-> 바닥
def move(dir):
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif dir == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]

command = deque(list(map(int, input().split())))
delta = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}
while command:
    dir = command.popleft()
    dx, dy = delta[dir]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M:
        move(dir)
        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[0]

        else:
            dice[0] = arr[nx][ny]
            arr[nx][ny] = 0
        x, y = nx, ny
        print(dice[2])