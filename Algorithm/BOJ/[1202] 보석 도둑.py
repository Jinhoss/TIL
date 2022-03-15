import heapq
import sys
input = sys.stdin.readline

N,  K = map(int, input().split())
gem = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(gem, [weight, value])

bag = []
for _ in range(K):
    capacity = int(input())
    heapq.heappush(bag, capacity)

result = 0
capable_gem = []

while bag:
    capacity = heapq.heappop(bag)
    while gem and capacity >= gem[0][0]:
        weight, value = heapq.heappop(gem)
        heapq.heappush(capable_gem, -value)
    if capable_gem:
        result -= heapq.heappop(capable_gem)
    elif not gem:
        break
print(result)