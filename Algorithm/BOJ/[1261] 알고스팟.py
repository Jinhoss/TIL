import heapq
import sys
input = sys.stdin.readline


def dijkstra():
    q = []
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                cost = dist + arr[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
INF = int(1e9)
distance = [[INF] * M for _ in range(N)]
dijkstra()
print(distance[N - 1][M - 1])