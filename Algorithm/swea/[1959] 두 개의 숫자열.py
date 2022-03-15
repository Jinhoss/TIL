T=int(input())
for tc in range(1,T+1):
    alen,blen =map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    max_v=0
    for a,b in zip(A,B):
       	max_v+=a*b
    if alen<blen:
        for i in range(1,blen-alen+1):
            result=0
            for a,b in zip(A,B[i:i+alen]):
                result+=a*b
            if result>=max_v:
                max_v=result
    else:
        for i in range(1,alen-blen+1):
            result=0
            for a,b in zip(A[i:i+blen],B):
                result+=a*b
            if result>=max_v:
                max_v=result
    print('#%d %d'%(tc,max_v))
        
        