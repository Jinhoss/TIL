# import sys
# sys.stdin = open('input.txt')

def dfs(x, y, k):
    visit = [[False] * n for _ in range(n)]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visit[x][y] = True
    stack = []
    length = 1
    chance = 1
    max_length = 0
    stack.append((x, y, arr[x][y], length, chance, visit))
    # i, j 현재 지점, height: 현재 지점의 높이, length: 등산로의 길이, chance: 봉우리를 깎을 수 있는 기회, visit: 방문지점
    while stack:
        i, j, height, length, chance, visit = stack.pop()
        if length > max_length:
            max_length = length
        for idx in range(4):
            # deepcopy를 이용한다. # 배열의 크기가 크지 않아 시간이 오래 걸리지 않음
            visit2 = [lst[:] for lst in visit]
            di, dj = delta[idx]
            ni, nj = i + di, j + dj
            # 현재 높이보다 낮고 배열 밖을 벗어나지 않으며 방문한 지점이 아니라면 경로에 추가한다.
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj]<height and not visit2[ni][nj]:
                visit2[ni][nj] = True
                stack.append((ni, nj, arr[ni][nj], length + 1, chance, visit2))
            # 현재 높이보다는 낮지 않지만 chance가 있어서 높이를 깎는다면 이동이 가능할 때, 기회를 없애고 경로에 추가한다.
            elif 0 <= ni < n and 0 <= nj < n and arr[ni][nj] - k < height and chance and not visit2[ni][nj]:
                visit2[ni][nj] = True
                stack.append((ni, nj, height - 1, length + 1, 0, visit2))
    return max_length


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    start_lst = []
    max_v = 0
    # 가장 높은 값 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_v:
                max_v = arr[i][j]
    # 시작점 리스트를 만들어준다.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_v:
                start_lst.append((i,j))
    result = 0
    for start in start_lst:
        l = dfs(*start, k)
        if l > result:
            result = l
    print('#{} {}'.format(tc, result))

