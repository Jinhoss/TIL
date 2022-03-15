T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    result = 0
    if n%k:
        result = 1
    print('#{} {}'.format(tc, result))

