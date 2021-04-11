import sys

input = sys.stdin.readline
M, N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
animal_lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for x, y in animal_lst:
    start = 0
    end = len(lst) - 1
    while start < end:
        mid = (start + end) // 2
        if lst[mid] < x:
            start = mid + 1
        else:
            end = mid
    if abs(lst[end] - x) + y <= L or abs(lst[end - 1] - x) + y <= L:
        cnt += 1
print(cnt)


