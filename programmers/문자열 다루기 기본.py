def solution(s):
    if len(s)==4 or len(s)==6:
        try:
            int(s)
        except ValueError:
            answer= False
        else:
            answer=True
    else:
        answer=False
    return answer