def solution(N, stages):
    result={}
    l=len(stages)
    for i in range(N):
        if l!=0:
            result[i+1]=stages.count(i+1)/l
            l-=stages.count(i+1)
        else:
            result[i+1]=0
    
    return sorted(result,key=lambda x:result[x],reverse=True)