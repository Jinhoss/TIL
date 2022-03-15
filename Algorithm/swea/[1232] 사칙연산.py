import sys
sys.stdin = open('input.txt')

# 사칙연산
def operator(num1, num2, oper):
    if oper == '-':
        return num1 - num2
    elif oper == '+':
        return num1 + num2
    elif oper == '*':
        return num1 * num2
    else:
        return num1 / num2

for tc in range(1,11):
    N = int(input())
    depth = len(bin(N)) - 2
    tree = [0] * (1<<depth)
    command = {}
    for _ in range(N):
        x = list(input().split())
        # 연산이 담긴 노드와 숫자만 담긴 노드를 구별해서 처리
        if len(x) == 4:
            command[x[0]] = x[1:]
        else:
            tree[int(x[0])] = int(x[1])
    # 제일 끝 노드부터 차례대로 연산한다.
    for node in sorted(command.keys() , key = lambda x: int(x), reverse = True):
        child1, child2 = tree[int(command[node][1])], tree[int(command[node][2])]
        tree[int(node)] = operator(child1, child2, command[node][0])

    print('#{} {}'.format(tc, int(tree[1])))




