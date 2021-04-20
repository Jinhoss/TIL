def my_func():
    result = 0
    for b in B:
        before = None
        l = 0
        r = N - 1
        while l <= r:
            m = (l + r) // 2
            if b == A[m]:
                result += 1
                break
            elif b < A[m]:
                r = m - 1
                current = 'left side'
            elif b > A[m]:
                l = m + 1
                current = 'right side'
            if before == current:
                break
            before = current
    return result

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = map(int, input().split())
    print('#{} {}'.format(test_case, my_func()))