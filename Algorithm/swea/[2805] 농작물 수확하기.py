# import sys
# sys.stdin=open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n=int(input())
    if n==1:
        arr=int(input())
        print('#{} {}'.format(tc, arr))
    else:
        arr = [list(input()) for _ in range(n)]
        result=0
        for i in range(n//2):
            for x in arr[i][n//2-i:n//2+1+i]:
                result+=int(x)
            for y in arr[-i-1][n//2-i:n//2+1+i]:
                result+=int(y)
        for lst in arr[n//2]:
            for x in lst:
                result+=int(x)
        print('#{} {}'.format(tc,result))


