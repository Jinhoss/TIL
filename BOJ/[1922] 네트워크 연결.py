import sys
input = sys.stdin.readline

# 최소 신장 트리
# 크루스칼 알고리즘
# 특정 원소가 속한 집합을 찾음
def find_parent(parent, x):
    # 루트 노트가 아니라면 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수
N = int(input())
# 간선의 개수
M = int(input())
# 부모 테이블 초기화
parent = [0] * (N + 1)
edges = []
result = 0
# 부모를 자기 자신으로 초기화
for i in range(N + 1):
    parent[i] = i

# cost 순으로 정렬하기 위해 cost를 앞으로 빼서 담음
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보 cost 순으로 정렬
edges.sort()

# 간선을 돌며 체크
for edge in edges:
    cost, a, b = edge
    # 사이클을 생성하지 않으면 Union 연산을 수행하고 cost를 결과값에 담아준다.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)