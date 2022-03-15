T=int(input())
def solution(n):
    if n%2==0:
        return 0, n//2
    elif n%3==0:
        return 1, n//3
    elif n%5==0:
        return 2, n//5
    elif n%7==0:
        return 3, n//7
    else:
        return 4, n//11
    
for tc in range(1,T+1):
    lst=[0, 0, 0, 0, 0]
    n=int(input())
    while n>1:
        idx, n=solution(n)
        lst[idx]+=1
    print('#%d'%tc, end=' ')
    print(*lst)