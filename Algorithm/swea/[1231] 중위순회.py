import sys
sys.stdin = open('input.txt')

def inorder(node):
    global result
    info = tree[int(node)]
    if len(info) == 4:
        inorder(info[2])
        result += info[1]
        inorder(info[3])
    elif len(info) == 3:
        inorder(info[2])
        result += info[1]
    else:
        result += info[1]


for tc in range(1, 11):
    N = int(input())
    tree = [[0]] + [list(map(str, input().split())) for _ in range(N)]
    result = ''
    inorder('1')
    print('#{} {}'.format(tc, result))

