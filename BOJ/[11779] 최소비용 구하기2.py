import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    path = [-1] * (V + 1)
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nxt in graph[now]:
            cost = nxt[1] + dist
            if cost <= distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))
                path[nxt[0]] = now
    return distance[end], path
if __name__ == '__main__':

    INF = 1e9
    V = int(input())
    E = int(input())
    graph = [[] for _ in range(V + 1)]
    distance = [INF] * (V + 1)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())
    path_result = [end]
    temp = end
    costResult, path = dijkstra(start)
    while path[temp] != -1:
        path_result.append(path[temp])
        temp = path[temp]
    print(costResult)
    print(len(path_result))
    print(*path_result[::-1])

