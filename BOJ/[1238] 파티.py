import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    INF = int(1e9)
    distance = [INF] * N
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
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

N, M, x = map(int, input().split())
graph = [[] for _ in range(N)]
INF = int(1e9)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
answer = [0] * N
for i in range(N):
    dist_lst = dijkstra(i)
    if i == x - 1:
        for idx, val in enumerate(dist_lst):
            answer[idx] += val
    else:
        answer[i] += dist_lst[x - 1]

print(max(answer))