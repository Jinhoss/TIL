# import sys
# sys.stdin=open("subset_input.txt")

#인풋 입력
T=int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    #1~12를 담고 있는 집합 A
    A = list(range(1, 13))
    cnt = 0
    #부분집합 생성
    for i in range(1 << 12):
        subset = []
        sum_v = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
                sum_v += A[j]
        #부분집합 원소의 개수가 N이고 합이 K이면 cnt값 1증가
        if len(subset) == N and sum_v == K:
            cnt += 1
    print('#{} {}'.format(tc,cnt))

