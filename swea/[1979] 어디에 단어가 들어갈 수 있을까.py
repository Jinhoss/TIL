# import sys
# sys.stdin=open("where_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num_cnt = [0] * (N + 1)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 탐색
    for i in range(N):
        before = 0
        cnt = 0
        for j in range(N):
            if before == 0 and arr[i][j] == 1:
                if cnt:
                    num_cnt[cnt] += 1
                cnt = 1
            elif before == 1 and arr[i][j] == 1:
                cnt += 1
            before = arr[i][j]
        if cnt:
            num_cnt[cnt] += 1

    # 세로 탐색
    for j in range(N):
        before = 0
        cnt = 0
        for i in range(N):
            if before == 0 and arr[i][j] == 1:
                if cnt:
                    num_cnt[cnt] += 1
                cnt = 1
            elif before == 1 and arr[i][j] == 1:
                cnt += 1
            before = arr[i][j]
        if cnt:
            num_cnt[cnt] += 1

    print('#{} {}'.format(tc, num_cnt[K]))
