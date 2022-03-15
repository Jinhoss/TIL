# import sys
# sys.stdin=open('input.txt')

def arr90(arr, n):
    result = []
    for j in range(n):
        lst = []
        for i in range(n-1 ,-1, -1):
            lst.append(arr[i][j])
        result.append(lst)
    return result

def arr180(arr,n):
    result = []
    for i in range(n-1, -1 ,-1):
        lst = []
        for j in range(n-1 ,-1 ,-1):
            lst.append(arr[i][j])
        result.append(lst)
    return result

def arr270(arr,n):
    result=[]
    for j in range(n-1, -1, -1):
        lst = []
        for i in range(n):
            lst.append(arr[i][j])
        result.append(lst)
    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    a, b, c = arr90(arr,n), arr180(arr,n), arr270(arr,n)
    print('#{}'.format(tc))
    for l90, l180, l270 in zip(a, b, c):
        print(''.join(l90), ''.join(l180), ''.join(l270))