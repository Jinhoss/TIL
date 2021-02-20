T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    check = [0] * len(lst)
    check[0]=int(lst[0])
    for i in range(1, len(lst)):
        if lst[i]!=lst[i-1]:
            check[i]+=(check[i-1]+1)
        else:
            check[i]=check[i-1]
    print('#{} {}'.format(tc, check[-1]))
