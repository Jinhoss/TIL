# import sys
# sys.stdin = open('input.txt')
#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #복도값 초기화
    corridor=[0]*400
    #학생 한명씩 돌면서 지나간 복도에 값을 1씩 추가한다.
    for _ in range(N):
        x, y = map(int,input().split())
        if x<=y:
            start = (x-1)//2
            end = (y-1)//2
        else:
            start = (y-1)//2
            end = (x-1)//2

        for idx in range(start, end+1):
            corridor[idx]+=1
    #복도에 저장된 값 중 최대값을 출력
    max_v = 0
    for v in corridor:
        if v>max_v:
            max_v=v
    print('#{} {}'.format(tc, max_v))



