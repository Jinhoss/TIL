T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check_lst = [False] * (N*N + 1)
    min_v, max_v, count = 0, 0, 0
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x in range(N):
        for y in range(N):
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
                    check_lst[arr[x][y]] = True
                    break
    for i in range(N*N - 1, -1, -1):
        if check_lst[i]:
            count += 1
        elif count:
            if count >= max_v:
                max_v = count
                min_v = i + 1
            count = 0
    print('#{} {} {}'.format(tc, min_v, max_v + 1))
