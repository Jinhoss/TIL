# import sys
# sys.stdin=open("binary_input.txt")

#이진탐색 구현 start:페이지 시작값, end:페이지 끝값, target: 목표값, cnt: 찾기위해 이진탐색 반복한 횟수
def binary_search(start,end,target,cnt):
    m=(start+end)//2
    if m==target:
        return cnt
    if target>m:
        return binary_search(m,end,target,cnt+1)
    else:
        return binary_search(start,m,target,cnt+1)
#입력값 인풋
T=int(input())
for tc in range(1,T+1):
    P, A, B = map(int,input().split())
    # A와 B 각각 실행 후, 횟수가 적은 사람이 승자
    cnt_A=binary_search(1,P,A,0)
    cnt_B=binary_search(1,P,B,0)
    if cnt_A>cnt_B:
        print('#{} B'.format(tc))
    elif cnt_A==cnt_B:
        print('#{} 0'.format(tc))
    else:
        print('#{} A'.format(tc))