# import sys
# sys.stdin = open('input.txt')

# 부모 탐색
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 부모 union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 테케 수 입력
T = int(input())
for tc in range(1, T + 1):
    # 노드의 개수
    N = int(input())
    # 노드 x좌표, y좌표
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    # 환경 부담 세율 실수
    E = float(input())
    # 간선과 이동 비용을 담을 리스트
    edges = []
    # 문제에서 요구한 형태로 거리를 계산하고 edges에 간선 정보를 담는다.
    # dist를 기준으로 정렬하기 위해 dist를 먼저 담음
    for i in range(N):
        for j in range(i, N):
            dist = ((x_lst[i] - x_lst[j])**2 + (y_lst[i] - y_lst[j])**2) * E
            edges.append((dist, i, j))
    # 비용이 작은 순으로 정렬
    edges.sort()
    parent = list(range(N))
    answer = 0
    for edge in edges:
        dist, i, j = edge
        # 사이클이 없으면 합쳐주고 거리를 결과 값에 더해준다.
        if find_parent(parent, i) != find_parent(parent, j):
            union_parent(parent, i, j)
            answer += dist
    print('#{} {}'.format(tc, round(answer)))
