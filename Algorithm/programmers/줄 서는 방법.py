def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        cnt = 1
        for i in range(1, n + 1):
            cnt *= i
        return cnt

def solution(n, k):
    answer = []
    lst = [i for i in range(1, n + 1)]
    while n:
        total = factorial(n) // n
        idx = k // total
        k = k % total
        if not k:
            answer.append(lst.pop(idx-1))
        else :
             answer.append(lst.pop(idx))
        n -= 1
        
    return answer