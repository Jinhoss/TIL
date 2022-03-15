for tc in range(1,11):
    t=int(input())
    result=0
    lst=list(map(int,input().split()))
    for i in range(2,t-2):
        max_v=0
        for j in [-2,-1,1,2]:
            if max_v<lst[i+j]:
                max_v=lst[i+j]
        if max_v<lst[i]:
            result+=(lst[i]-max_v)
    print('#%d %d'%(tc,result))
        
                
            
            
                 