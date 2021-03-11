from collections import deque
# import sys
# sys.stdin = open('input.txt')

# 깊이가 주어졌을 때 bfs로 탐색할 수 있는 범위를 구하는 문제이다
# bfs를 구현하는 것은 어렵지 않지만 통로를 구현하는 것이 쉽지가 않았다.
def bfs(r, c):
    global l
    # 해당 통로에서 이동 가능한 방향을 딕셔너리 형태로 담았다.
    tunnel = {
        0: (),
        1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
        2: ((1, 0), (-1, 0)),
        3: ((0, 1), (0, -1)),
        4: ((-1, 0), (0, 1)),
        5: ((1, 0), (0, 1)),
        6: ((1, 0), (0, -1)),
        7: ((-1, 0), (0, -1))
    }
    # 큐를 이용해 bfs 구현
    q = deque()
    q.append((r, c, 1))
    visit[r][c] = True
    cnt = 0
    while q:
        x, y, time = q.popleft()
        if time <= l:
            cnt+=1
        if time == l:
            continue
        for d in tunnel[arr[x][y]]:
            dx, dy = d
            nx, ny = x + dx, y + dy
            # 다음 목표 지점의 통로가 현재 지점과 이어지는지 확인하기 위해 다음 통로에서 현재 지점으로 올 수 있는지를 확인
            # 다음 지점에서 역방향으로 이동 가능하면 이어져있는 것으로 간주
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and (-dx,-dy) in tunnel[arr[nx][ny]]:
                visit[nx][ny] = True
                q.append((nx, ny, time + 1))
    return cnt



T = int(input())
for tc in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    cnt = bfs(r, c)
    print('#{} {}'.format(tc, cnt))

