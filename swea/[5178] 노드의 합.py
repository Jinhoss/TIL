import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [-1] * (N + 1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    for idx in range(N-M, 0, -1):
        if idx*2 <N:
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        else:
            tree[idx] = tree[idx*2]
    print('#{} {}'.format(tc, tree[L]))