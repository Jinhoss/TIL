import sys
input = sys.stdin.readline

V, E = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
parent = list(range(V + 1))
edges = []
for _ in range(E):
    v, e, cost = map(int, input().split())
    edges.append((cost, v, e))

edges.sort()
result = 0
edge_count = 0
for edge in edges:
    if edge_count == V - 2:
        break
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        edge_count+=1
print(result)