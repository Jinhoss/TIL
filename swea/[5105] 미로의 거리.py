from collections import deque
# import sys
# sys.stdin = open('input.txt')
# 테스트케이스 입력
T = int(input())
def bfs(si, sj, ei, ej):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    Q = deque()
    Q.append((si,sj))
    while Q:
        x, y = Q.popleft()
        visit[x][y] = True
        # 4가지 방향에 대해 이동가능 여부 확인
        for i in range(4):
            dx, dy = delta[i]
            nx, ny = x+dx, y+dy
            # 이동이 가능하다면 출발점에서 떨어져있는 칸 수를 기록한다.
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] == 0:
                Q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
            # 도착한다면 몇 칸을 이동하여 도착하였는지 저장
            elif 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] == 3:
                distance[nx][ny] = distance[x][y]
    return distance[ei][ej]


for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    visit = [[False]* n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    # 출발점, 도착점 저장
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j

    print('#{} {}'.format(tc, bfs(si, sj, ei, ej)))