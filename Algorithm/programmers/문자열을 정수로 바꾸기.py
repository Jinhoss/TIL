def solution(s):
    answer=0
    x=s.split('-')
    if x[0]=='-':
        y=x[1:]
        answer-=int(y)
    else:
        answer+=int(s)
    return answer