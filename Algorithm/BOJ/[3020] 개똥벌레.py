import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# 누적 합으로 해결하는 풀이도 있음
N, H = map(int, input().split())
top = []
bottom = []

# 순서에 따라 석순은 bottom, 종유석은 top에 저장
for i in range(N):
    num = int(input())
    if i%2:
        top.append(H - num + 1)
    else:
        bottom.append(num)
# 길이와 bisect index값을 이용해서 높이에 따라 격파되는 돌의 개수를 카운트
# 따라서 돌의 개수를 저장
b_len = N // 2
t_len = N // 2
# 이분탐색을 위한 정렬
top.sort()
bottom.sort()
# 높이에 따른 격파 갯수를 total list에 저장
total = [0] * (H + 1)
# 석순은 전체 길이에서 하한값을 빼면 갯수가 나오고 종유석은 상한값을 구하면 갯수가 나온다.
for height in range(1, H + 1):
    total[height] = (b_len - bisect_left(bottom, height)) + bisect_right(top, height)
# 높이가 0인 경우 제외
total = total[1:]
# 최소 격파 갯수 값
ans = min(total)
print(ans, total.count(ans))