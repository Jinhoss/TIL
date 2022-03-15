# import sys
# sys.stdin = open('input.txt')

# 투 포인터를 이용해 구현
n, m = map(int, input().split())
lst = list(map(int, input().split()))

# count : 합이 m인 부분 수열의 갯수
count = 0
# interval_sum : 부분 수열의 합
interval_sum = 0
# 부분 수열의 마지막 인덱스
end = 0


# start를 부분 수열의 첫 번째 인덱스로 둔다.
for start in range(n):
    # end를 끝까지 이동시켜가며 만족하는 부분 수열의 합이 있는지 조사
    while interval_sum < m and end < n:
        interval_sum += lst[end]
        end += 1
    # 있다면 초기화 카운트 +1 후 interval_sum 초기화
    if interval_sum == m:
        count+=1
    interval_sum -= lst[start]
print(count)

