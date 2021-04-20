def dfs(queen, idx, n):
    cnt = 0
    if n == idx:
        return 1
    for col in range(n):
        queen[idx] = col
        check = True
        for i in range(idx):
            if queen[i] == queen[idx]:
                check = False
                break
            if abs(queen[i]-queen[idx]) == idx - i:
                check = False
                break
        if check:
            cnt += dfs(queen, idx + 1, n)
    return cnt
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    result = dfs([0] * n, 0, n)
    print('#{} {}'.format(tc, result))