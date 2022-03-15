import sys
sys.stdin = open('input.txt')

def preorder(node):
    global cnt
    cnt+=1
    if not tree.get(node, 0):
        return
    if len(tree[node]) == 1:
        preorder(tree[node][0])
    if len(tree[node]) == 2:
        preorder(tree[node][0])
        preorder(tree[node][1])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = {}
    lst = list(map(int, input().split()))
    for idx in range(E):
        v, e = lst[idx * 2], lst[idx * 2 + 1]
        tree[v] = tree.get(v, []) + [e]
    cnt = 0
    preorder(N)
    print('#{} {}'.format(tc, cnt))