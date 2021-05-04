import sys
sys.setrecursionlimit(1000000)

n = int(input())
in_ord = list(map(int, input().split()))
post_ord = list(map(int, input().split()))

pre = [0] * (n + 1)

for i in range(n):
    pre[in_ord[i]] = i

def divide(in_l, in_r, p_l, p_r):
    if (in_l > in_r) or (p_l > p_r):
        return
    # 부모 노드 탐색
    root = post_ord[p_r]
    print(root, end = " ")

    # 왼쪽 인자 갯수
    left = pre[root] - in_l
    # 오른쪽 인자 갯수
    right = in_r - pre[root]

    # 왼쪽 노드, 오른쪽 노드
    divide(in_l, in_l + left - 1, p_l, p_l + left - 1)
    divide(in_r - right + 1, in_r, p_r - right, p_r - 1)

divide(0, n - 1, 0, n - 1)
