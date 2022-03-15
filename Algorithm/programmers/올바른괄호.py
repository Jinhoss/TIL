def solution(s):
    sum_v=0
    for i in s:
        if i=="(":
            sum_v+=1
        else:
            sum_v-=1
        if s<0:
            break
    if not sum_v:
        answer=True
    else:
        answer=False
        return answer