# 수열을 돌며 좋은 수열인지 확인
def check(result, idx):
    for k in range(idx):
        sliceTemp = result[k:]
        for i in range(1, len(sliceTemp)//2 + 1):
            checkV = sliceTemp[:i]
            if checkV == sliceTemp[i:i+i]:
                return False
    return True

def sol(idx):
    # 좋은 수열이 아닌 경우
    if not check(result, idx):
        return -1
    # 좋은 수열인 경우 1, 2, 3 순으로 진행하기 때문에 만족하는 최초 값이 가장 작은 좋은 수열이다.
    if idx == N:
        print(*result, sep="")
        return 0
    # 백트래킹으로 확인
    for i in range(1,4):
        result.append(i)
        if sol(idx+1) == 0:
            return 0
        result.pop()

N = int(input())
result = []
sol(0)