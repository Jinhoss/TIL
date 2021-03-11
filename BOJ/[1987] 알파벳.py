import sys
input = sys.stdin.readline().strip
#pypy3로 제출
def dfs(x, y, d):
    global max_v
    if d > max_v:
        max_v = d
    for i in range(4):
        dx, dy = delta[i]
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not visit[lst[nx][ny]]:
            visit[lst[nx][ny]] = True
            dfs(nx, ny, d+1)
            visit[lst[nx][ny]] = False

r, c = map(int, input().split())
lst = [list(map(lambda x:ord(x)-65,input())) for _ in range(r)]
visit = [False] * 26
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_v = 1
visit[lst[0][0]] = True
dfs(0, 0, 1)
print(max_v)

