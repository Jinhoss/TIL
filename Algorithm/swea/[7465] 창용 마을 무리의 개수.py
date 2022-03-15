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



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = list(range(N + 1))
    for _ in range(M):
        x, y = map(int, input().split())
        union_parent(parent, x, y)
    group = set()
    for i in range(1, N + 1):
        group.add(find_parent(parent, i))

    print('#{} {}'.format(tc, len(group)))
