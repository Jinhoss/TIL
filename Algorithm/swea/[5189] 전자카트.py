# import sys
# sys.stdin = open('input.txt')

T = int(input())

def dfs(before, cnt, value):
    global result
    if value > result:
        return
    if cnt == N - 1:
        if value + arr[before][0] < result:
            result = value + arr[before][0]
            return

    for idx in range(1, N):
        if idx == before:
            continue
        if not visit[idx]:
            visit[idx] = True
            dfs(idx, cnt + 1, value + arr[before][idx])
            visit[idx] = False

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    result = int(1e9)
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, result))