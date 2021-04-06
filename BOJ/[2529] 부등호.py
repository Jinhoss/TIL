k = int(input())
lst = list(input().split())
visit = [False] * 10
min_v, max_v = '', ''

def check(n, m, sign):
    if sign == '<':
        return n < m
    else:
        return n > m

def solution(cnt, answer):
    global min_v, max_v
    if cnt == k + 1:
        # 0부터 돌기 때문에 처음 등장한 값이 min_v
        if not len(min_v):
            min_v = answer
        # 가장 마지막으로 만족한 값이 max_v
        else:
            max_v = answer
        return
    for i in range(10):
        if not visit[i]:
            if cnt == 0 or check(int(answer[-1]), i, lst[cnt - 1]):
                visit[i] = True
                solution(cnt + 1, answer + str(i))
                visit[i] = False
solution(0, '')
print(max_v)
print(min_v)
