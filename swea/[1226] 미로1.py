from collections import deque
# bfs함수
def bfs(si, sj):
    q = deque([(si, sj)])
    #방향
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        x, y = q.popleft()
        #방문 여부 저장
        visit[x][y] = 1
        # 방향을 돌며 이동가능한지 파악
        for i in range(4):
            dx, dy = delta[i]
            nx, ny = x+dx, y+dy
            # 다음 구간이 통로인 0이라면 q에 추가
            if 0 <= nx < 16 and 0 <= ny < 16 and not visit[nx][ny] and arr[nx][ny] == 0:
                q.append((nx,ny))
            # 다음 구간이 도착지점인 3이라면 도착가능
            elif 0 <= nx < 16 and 0 <= ny < 16 and not visit[nx][ny] and arr[nx][ny] == 3:
                return 1
    return 0


for tc in range(1, 11):
    input()
    arr = [list(map(int, input())) for _ in range(16)]
    visit = [[0]*16 for _ in range(16)]
    # 시작지점 탐색
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si, sj = i, j
    print('#{} {}'.format(tc, bfs(si, sj)))
