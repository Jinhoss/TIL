N = int(input())
lst = list(map(int, input().split()))
x = int(input())
lst.sort()
start, end = 0, N - 1
cnt = 0
while start < end:
    sub_sum = lst[start] + lst[end]
    if sub_sum == x:
        cnt += 1
    if sub_sum < x:
        start += 1
        continue
    end -= 1
print(cnt)