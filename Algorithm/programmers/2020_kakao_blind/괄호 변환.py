def split(p):
    if p=='':
        return ''
    else:
        count=0
        for i,k in enumerate(p):
            if k=='(':
                count+=1
            else:
                count-=1
            if count==0:
                break
        return p[:i+1],p[i+1:]

def check(p):
    count=0
    for i in p:
        if i=='(':
            count+=1
        else:
            count-=1
        if count<0:
            return False
    return True
def solution(p):
    try:
        u,v=split(p)
    except:
        return ''
    answer=''
    if check(u):
        answer+=u
        answer+=solution(v)
        return answer
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        u=u[1:-1]
        print(answer)
        for i in u:
            if i=='(':
                answer+=')'
            else:
                answer+='('
    return answer