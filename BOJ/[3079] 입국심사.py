import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
left, right = 1, max(lst) * M
result = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for x in lst:
        cnt += mid//x
        if cnt >= M:
            result = mid
            right = mid - 1
            break
    if cnt < M:
        left = mid + 1
print(result)