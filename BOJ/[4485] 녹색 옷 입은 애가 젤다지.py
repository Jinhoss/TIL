import sys
import heapq
input = sys.stdin.readline

def dijkstra(i, j):
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = []
    distance[i][j] = graph[i][j]
    heapq.heappush(q, (graph[i][j], i, j))
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    print('Problem {}: {}'.format(tc, distance[N - 1][N - 1]))
    tc+=1
