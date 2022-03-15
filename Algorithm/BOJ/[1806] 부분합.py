import sys
sys.stdin = open('input.txt')

n, s = map(int, input().split())
num_lst = list(map(int, input().split()))

end = 0
min_length = n+1
interval_sum = 0
check = False
for start in range(n):
    while (interval_sum < s) and (end < n):
        interval_sum += num_lst[end]
        end+=1
    length = end - start
    if interval_sum>=s and length < min_length:
        check = True
        min_length = length
    interval_sum-=num_lst[start]
if check:
    print(min_length)
else:
    print(0)