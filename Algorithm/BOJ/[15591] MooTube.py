from collections import deque
def find_video(start, k, graph):
    q = deque()
    q.append((start, float('inf')))
    visit = [0] * N
    visit[start] = 1
    cnt = 0
    while q:
        x, min_dist = q.popleft()
        for nx, dist in graph.get(x, []):
            if visit[nx] == 1:
                continue
            if min_dist > dist:
                q.append((nx, dist))
                if dist >= k:
                    cnt += 1
            else:
                q.append((nx, min_dist))
                if min_dist >= k:
                    cnt += 1
            visit[nx] = 1
    return cnt

N, K = map(int, input().split())
graph = {}
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a - 1] = graph.get(a - 1, []) + [(b - 1, c)]
    graph[b - 1] = graph.get(b - 1, []) + [(a - 1, c)]

for _ in range(K):
    k, v = map(int, input().split())
    print(find_video(v - 1, k, graph))

