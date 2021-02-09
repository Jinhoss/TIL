#테스트 케이스 수 입력
T=int(input())
for tc in range(1,T+1):
    #리스트 길이와 리스트 입력
    l=int(input())
    lst=list(map(int,input().split()))
    #최소값 최대값 초기화
    min_v=1000000
    max_v=0
    #리스트를 돌며 최대값과 최소값 저장
    for i in lst:
        if i>max_v:
            max_v=i
        if i<min_v:
            min_v=i
     #결과 출력
    print('#{} {}'.format(tc,max_v-min_v))