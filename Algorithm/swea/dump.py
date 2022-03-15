def min_max(lst):
    max_v = 0
    max_idx = 0
    min_v = 101
    min_idx = 0
    for i in range(len(lst)):
        if lst[i]>max_v:
            max_v=lst[i]
            max_idx=i
        if lst[i] < min_v:
            min_v = lst[i]
            min_idx = i
    return max_v,max_idx,min_v,min_idx


for tc in range(1,11):
    dump=int(input())
    lst=list(map(int,input().split()))
    while dump>0:
        max_v,max_idx,min_v,min_idx=min_max(lst)
        lst[max_idx]-=1
        lst[min_idx]+=1
        dump-=1
    max_v, max_idx, min_v, min_idx = min_max(lst)
    print('#{} {}'.format(tc, max_v-min_v))