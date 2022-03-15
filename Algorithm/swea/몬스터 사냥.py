t=int(input())
for tc in range(t):
    dmg_lst=list(map(int,input().split()))
    result=0
    for i in range(dmg_lst[2]):
        result+=dmg_lst[0]*(1+dmg_lst[1]*(i/100))
    print('#%d %d'%(tc+1,result))