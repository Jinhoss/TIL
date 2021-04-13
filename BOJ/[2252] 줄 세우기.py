from collections import deque
import sys

# sys.stdin.readline을 쓰고 안쓰고 속도 차이가 큰 편, 안써도 통과는 됨
# 안쓰는 경우 : 4000ms , 쓸 경우: 260ms
input = sys.stdin.readline
def topology_sort():
    q = deque()
    # 진입차수가 0인 노드를 큐에 담음
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q: # 큐가 빌 때까지
        x = q.popleft()
        result.append(x)
        # 연결된 노드들의 진입차수 1씩 감소
        for idx in graph[x]:
            indegree[idx] -= 1
            # 진입차수가 0이 되면 다시 큐에 담음
            if indegree[idx] == 0:
                q.append(idx)
    # 결과 출력
    print(*result)

# 노드의 개수, 간선의 개수
N, M = map(int, input().split())
# 연결 리스트 초기화
graph = [[] for _ in range(N + 1)]
# 진입차수 초기화
indegree = [0] * (N + 1)
# 방향 그래프 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort()
