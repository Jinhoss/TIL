# 주어

N, L = map(int, input().split())
num = [0] * 1001
lst = list(map(int, input().split()))
for i in lst:
    num[i] = 1

cnt = 0
for idx in range(1001):
    if num[idx]:
        for i in range(idx, min(1001, idx + L)):
            num[i] = 0
        cnt+=1
print(cnt)

