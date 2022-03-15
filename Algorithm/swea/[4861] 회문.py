# import sys
# sys.stdin = open("input2.txt")

#회문검사 함수
def check(lst):
    for i in range(len(lst)//2):
        if lst[i]!=lst[-i-1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = N-M+1
    arr = [list(input()) for _ in range(N)]
    result = ''
    #행 먼저 회문을 검사한다.
    for s in arr:
        for i in range(num):
            if check(s[i:i+M]):
                result=s[i:i+M]
                break
    #행 검사가 끝난 후에도 결과를 찾지 못했다면 열에 대해서 검사를 한다.
    if not result:
        for s in list(zip(*arr)):
            for i in range(num):
                if check(s[i:i+M]):
                    result=s[i:i+M]
    print('#{}'.format(tc),''.join(result))
