def solution(n,a,b):
    x=a-1
    y=b-1
    answer=0
    while x!=y:
        x=(x//2)
        y=(y//2)
        answer+=1
    return answer