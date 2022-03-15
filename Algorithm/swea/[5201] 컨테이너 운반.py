T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    w.sort(reverse=True)
    truck.sort(reverse=True)
    answer = 0
    check = []
    for w_truck in truck:
        for weight in w:
            if w_truck >= weight:
                check.append(weight)
                w.remove(weight)
                break
    if not check:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(check)))
