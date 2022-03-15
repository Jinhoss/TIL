import sys
input = sys.stdin.readline
# 서로소 집합의 경로 압축 구현
# 백준 서버 재귀한도가 1000이라 runtime error가 뜸, 100000으로 늘렸을때 해결되었음
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
# 노드의 부모 노드를 찾는 함수
def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
# 부모 노드의 숫자가 작은 쪽으로 합쳐준다.
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = list(range(n+1))

for _ in range(m):
    c, v, e = map(int, input().split())
    if c:
        if find_parent(v) == find_parent(e):
            print('YES')
        else:
            print('NO')
    else:
        union_parent(v, e)


