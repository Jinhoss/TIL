import sys
sys.stdin = open('input.txt')

def dfs(start, end):
    i, j = start
    ei, ej = end
    stack=[]
    visit = [[0] * N for _ in range(N)]
    delta=[(0,1), (1,0), (-1,0), (0,-1)]
    stack.append((i,j))
    while stack:
        x, y = stack.pop()
        visit[x][y] = 1
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<=N-1 and 0<=ny<=N-1 and arr[nx][ny]==0 and visit[nx][ny]==False:
                stack.append((nx,ny))
            elif 0<=nx<=N-1 and 0<=ny<=N-1 and arr[nx][ny]==3:
                visit[nx][ny]=1
    return visit[ei][ej]
T = int(input())
for tc in range(1, T+1):
    N=int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                start = (i,j)
            elif arr[i][j]==3:
                end = (i,j)
    print('#{} {}'.format(tc, dfs(start,end)))


