import heapq
import sys
input = sys.stdin.readline

n = int(input())
left, right = [], []
for _ in range(n):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    if right and -left[0] > right[0]:
        l_v = -heapq.heappop(left)
        r_v = heapq.heappop(right)
        heapq.heappush(left, -r_v)
        heapq.heappush(right, l_v)
    print(-left[0])
