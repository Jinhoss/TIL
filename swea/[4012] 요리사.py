# import sys
# sys.stdin = open('input.txt')
# 백준 14889와 같은 문제
def combi(idx, t1):
    global min_v
    l = N//2
    if len(t1) > l:
        return
    # 기존의 최소값보다 작다면 최소값 갱신
    if len(t1) == l:
        sum1 = 0
        sum2 = 0
        t2 = [x for x in num_lst if x not in t1]
        for m1 in t1:
            for m2 in t1:
                sum1+=arr[m1][m2]
        for m1 in t2:
            for m2 in t2:
                sum2+=arr[m1][m2]
        if abs(sum1-sum2) < min_v:
            min_v = abs(sum1-sum2)
    if idx == N:
        return
    combi(idx + 1, t1)
    t2 = t1 + [num_lst[idx]]
    combi(idx + 1, t2)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num_lst = list(range(N))
    min_v = float('inf')
    combi(0, [])
    print('#{} {}'.format(tc, min_v))

