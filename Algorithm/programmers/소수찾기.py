def solution(n):
    m=n+1
    x=[False,False]+[True]*(n-1)
    
    for i in range(2,n+1):
        if x[i]==True:
            for j in range(2*i,n+1,i):
                x[j]=False
                
    return x.count(True)