from collections import deque
# import sys
# sys.stdin = open('input.txt')
# bfs구현
def bfs(start, end):
    q = deque([(start,0)])
    while q:
        x, cnt = q.popleft()
        visit[x] = True #방문여부 저장
        #각 노드에서 갈 수 있는 점들을 확인
        for dx in vertex[x]:
            if not visit[dx] and dx == end:
                return cnt+1
            # 도착 지점이 아니라면 거리를 1 증가하여 저장
            elif not visit[dx]:
                q.append((dx, cnt+1))
    return 0
# 테스트케이스 입력
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    vertex = {}
    visit = [False] * (V+1)
    # 각 노드에서 갈 수 있는 노드의 정보를 저장
    for _ in range(E):
        i, j = map(int, input().split())
        vertex[i] = vertex.get(i , []) + [j]
        vertex[j] = vertex.get(j, []) + [i]
    start, end = map(int, input().split())
    print('#{} {}'.format(tc, bfs(start,end)))
