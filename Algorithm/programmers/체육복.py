def solution(n, lost, reserve):
    answer=0
    x=set(reserve)-set(lost)
    y=set(lost)-set(reserve)
    for i in x:
        if i-1 in y:
            y.remove(i-1)
        elif i+1 in y:
            y.remove(i+1)
            
            
    return n-len(y)