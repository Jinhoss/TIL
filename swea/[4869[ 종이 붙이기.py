T = int(input())
for tc in range(1, T+1):
    n = int(input())//10
    arr = [0] * (n+1)
    arr[0], arr[1] = 1, 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]*2
    print('#{} {}'.format(tc, arr[-1]))