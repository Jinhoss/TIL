T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x: (x[1], x[0]))
    result = []
    while lst:
        result.append(lst.pop(0))
        lst = [x for x in lst if x[0] >= result[-1][1]]
    print("#{} {}".format(tc, len(result)))