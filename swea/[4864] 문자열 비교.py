# import sys
# sys.stdin=open("input1.txt")


T = int(input())
for tc in range(1,T+1):
    N = input()
    M = input()
    #문제에서 요구한대로 문자열 N이 M에 있는지 확인하고 있다면 1 없다면 0을 반환
    if N in M:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))