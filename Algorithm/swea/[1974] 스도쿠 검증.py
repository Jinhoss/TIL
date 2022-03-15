T=int(input())

def sdoku(arr):
    for lst in arr:
        for x in range(1,10):
            if x not in lst:
                return False
    for lst in list(zip(*arr)):
        for x in range(1,10):
            if x not in lst:
                return False
    ans=0
    for x in range(0,7,3):
        for y in range(0,7,3):
            nums=list(range(1,10))
            cnt=0
            for i in range(3):
                for j in range(3):
                    if arr[i+x][j+y] in nums:
                        nums.remove(arr[i+x][j+y])
                        cnt+=1
            if cnt!=9:
                return False
    return True





for tc in range(1,T+1):
    arr=[list(map(int,input().split())) for _ in range(9)]
    if sdoku(arr):
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
