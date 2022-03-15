# import sys
# sys.stdin = open('input.txt')
# 최대한 라이브러리를 사용하지 않는 방식으로 풀어서 시간이 좀 걸립니다.
# itertools의 combinations을 사용하면 편리
# combination 구현
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

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num_lst = list(range(N))
# float('inf') 보다 주어진 제약 조건에 따라 최대값을 설정해주는게 좀 더 가볍다.
min_v = float('inf')
combi(0, [])
print(min_v)



