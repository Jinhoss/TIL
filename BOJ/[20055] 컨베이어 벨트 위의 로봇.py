import sys
input = sys.stdin.readline


# 벨트 회전
def rotation(lst):
    new = []
    new.append(lst.pop())
    new += lst
    return new


N, K = map(int, input().split())
lst = list(map(int, input().split()))
robot = [0] * (N * 2)
answer = 1
while True:
    lst = rotation(lst)
    robot = rotation(robot)
    robot[N - 1] = 0

    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and lst[i + 1] >= 1:
            lst[i + 1] -= 1
            robot[i + 1] = robot[i]
            robot[i] = 0
    robot[N - 1] = 0

    if not robot[0] and lst[0]:
        lst[0] -= 1
        robot[0] = 1
    cnt = 0
    for i in range(len(lst)):
        if not lst[i]:
            cnt += 1
    if cnt >= K:
        print(answer)
        break
    answer += 1
