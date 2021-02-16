#인풋 입력
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[['']*10 for _ in range(10)]
    #행렬을 돌며 color가 1이면 R color가 2이면 B를 추가
    for _ in range(n):
        x1,y1,x2,y2,color=map(int,input().split())
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if color==1:
                    arr[i][j]+='R'
                else:
                    arr[i][j]+='B'
    #행렬을 돌며 R가 B가 모두 있으면 보라색으로 간주하고 cnt+=1
    cnt=0
    for i in range(10):
        for j in range(10):
            if 'R' in arr[i][j] and 'B' in arr[i][j]:
                cnt+=1
    print('#{} {}'.format(tc,cnt))

