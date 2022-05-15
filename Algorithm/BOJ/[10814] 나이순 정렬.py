import heapq

N = int(input())
q = []
for idx in range(N):
    a, b = input().split()
    heapq.heappush(q, (int(a), idx, b))

while q:
    line = heapq.heappop(q)
    print(line[0], line[2])