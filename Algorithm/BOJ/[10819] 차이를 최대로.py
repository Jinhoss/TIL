from itertools import permutations
# import sys
# sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))
# 나올 수 있는 숫자의 배열들
num_lst = list(permutations(lst,N))
max_v = 0
# 문제에서 제시한 방법으로 더하기를 진행하며 합을 비교
for nums in num_lst:
    sum_v = 0
    for idx in range(N-1):
        sum_v += abs(nums[idx]-nums[idx+1])
    if sum_v > max_v:
        max_v = sum_v
print(max_v)
