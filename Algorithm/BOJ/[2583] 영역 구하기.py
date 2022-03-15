from collections import deque
# import sys
# sys.stdin = open('input.txt')

def bfs(i,j):
    q = deque()
    # 네 방향을 탐색
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    arr[i][j] = 1
    q.append((i,j))
    area = 0
    while q:
        #연결된 영역을 하나씩 카운트
        x, y = q.popleft()
        area += 1
        for idx in range(4):
            dx, dy = delta[idx]
            nx, ny = x + dx, y + dy
            # 배열을 벗어나지 않도록 설정
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
                q.append((nx,ny))
                arr[nx][ny]=1
    return area

M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

#주어진 사각형의 각 끝점을 이용해 배열에 사각형이 있는 부분을 표현한다.
for _ in range(K):
    si, sj, ei, ej = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = 1
ans = []
cnt = 0
for i in range(N):
    for j in range(M):
        # 배열 값이 0이라면 탐색을 시행한 횟수를 증가시켜주고 영역의 넓이를 탐색한다.
        if not arr[i][j]:
            cnt+=1
            ans.append(bfs(i,j))
print(cnt)
# 영역을 오름차순으로 정렬하여 출력한다.
print(*sorted(ans))
