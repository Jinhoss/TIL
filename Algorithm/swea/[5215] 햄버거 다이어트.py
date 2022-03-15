# import sys
# sys.stdin = open('input.txt')

# 각 재료에 대해서 넣는 경우, 안넣는 경우를 반복하며 칼로리를 넘지 않으며 최고의 점수 찾는다.
# 현재의 인덱스, 점수, 칼로리 상태를 인자로 받음
def check(idx, score, cal):
    global best_score
    # 정해진 칼로리를 넘어설 경우 리턴
    if cal > L:
        return
    # 최고 점수를 넘는다면 갱신해준다.
    if score > best_score:
        best_score = score
    # 인덱스가 N에 도달하면 리턴
    if idx == N:
        return
    # 재료를 넣지 않는 경우
    check(idx+1, score, cal)
    # 재료를 넣는 경우
    check(idx+1, score + lst[idx][0], cal+lst[idx][1])

#테스트케이스 입력
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    lst = []
    best_score = 0
    score = 0
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    check(0, 0, 0)
    print('#{} {}'.format(tc, best_score))
