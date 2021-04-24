import heapq
# import sys
# sys.stdin = open('input.txt')

# 우선순위 큐를 사용하면 O(ElogV), 사용하지 않으면 O(V**2)이다.
# 무한대 값
INF = float('inf')
# 다익스트라 구현
def dijkstra():
    q = []
    # q에 시작점의 거리, 시작 x좌표, 시작 y좌표를 담는다.
    heapq.heappush(q, (0, 0, 0))
    # 시작점의 거리는 0 으로 설정한다.
    distance[0][0] = 0
    # 이동 가능한 방향
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        # 최단 거리에 대한 정보를 꺼낸다.
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드이면 넘어간다.
        if distance[x][y] < dist:
            continue
        # 다음 좌표 탐색
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0<= nx < N and 0 <= ny < N:
                cost = dist + arr[nx][ny]
                # 다른 노드를 거쳐서 도달하는 것이 더 비용이 저렴하다면 갱신한다.
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x:int(x), list(input()))) for _ in range(N)]
    # 거리정보 무한대로 초기화
    distance = [[INF] * N for _ in range(N)]
    dijkstra()
    print('#{} {}'.format(tc, distance[N - 1][N - 1]))