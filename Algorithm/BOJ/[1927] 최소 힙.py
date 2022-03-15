import sys
import heapq
input = sys.stdin.readline


N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(q, x)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)