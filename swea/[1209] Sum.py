for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0
    for lst in arr:
        sum_v = 0
        for x in lst:
            sum_v += x
        if sum_v > max_v:
            max_v = sum_v
    for j in range(len(arr)):
        sum_v = 0
        for i in range(len(arr)):
            sum_v += arr[i][j]
        if sum_v > max_v:
            max_v = sum_v
    sum_v = 0
    for i in range(len(arr)):
        sum_v += arr[i][i]
    if sum_v > max_v:
        max_v = sum_v
    sum_v = 0
    for j in range(len(arr)-1, -1, -1):
        sum_v += arr[j][j]
    if sum_v > max_v:
        max_v = sum_v
    print('#{} {}'.format(tc, max_v))





