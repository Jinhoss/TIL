def solution(a, b):
    n=max(a,b)
    m=min(a,b)
    answer=0
    for i in range(m,n+1):
        answer+=i
    return answer