import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))
    return distance

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = int(1e9)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
result = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
result2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]

if result >= INF:
    print(-1)
else:
    print(min(result, result2))