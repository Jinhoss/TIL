import sys
sys.stdin = open('input.txt')

T = int(input())

def cal(idx, prob):
    global max_prob
    if prob <= max_prob:
        return
    if idx == N:
        if prob > max_prob:
            max_prob = prob
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            cal(idx + 1, prob * (lst[idx][i] / 100))
            visit[i] = False

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        p = list(map(int, input().split()))
        lst.append(p)
    max_prob = 0
    visit = [False] * N
    cal(0, 1)
    max_prob *= 100
    print('#%d %07f'%(tc, max_prob))