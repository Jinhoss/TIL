import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    q = []
    distance[start][0] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]][K - 1]:
                distance[node[0]][K - 1] = cost
                distance[node[0]].sort()
                heapq.heappush(q, (cost, node[0]))

N, M, K = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(N + 1)]
distance = [[INF] * K for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dijkstra(1)
for i in range(1, N + 1):
    if distance[i][K - 1] == INF:
        print(-1)
    else:
        print(distance[i][K - 1])
