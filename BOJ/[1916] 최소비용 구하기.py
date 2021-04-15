import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (node[0], cost))



N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
INF = float('inf')
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])