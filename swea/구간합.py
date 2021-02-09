#인풋 입력
T=int(input())
for tc in range(1,T+1):
    N, M=map(int,input().split())
    lst=list(map(int,input().split()))
    #최소값과 최대값 초기화
    min_v=float('inf')
    max_v=0
    #각 구간합을 돌며 최소값과 최대값 저장
    for i in range(N-M+1):
        inter_lst=lst[i:i+M]
        sum=0
        for j in inter_lst:
            sum+=j
        if sum>max_v:
            max_v=sum
        if sum<min_v:
            min_v=sum
    print('#{} {}'.format(tc,max_v-min_v))