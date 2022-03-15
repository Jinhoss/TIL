# import sys
# sys.stdin = open('input.txt')

def dfs(start, end):
    stack = []
    visit = [False] * (V+1)
    stack.append(start)
    # 입력받은 start부터 시작, 값이 있고 아직 방문하지 않은 정점이면 stack에 추가
    while stack:
        v = stack.pop()
        visit[v]=True
        for w in range(V+1):
            if not visit[w]:
                if arr[v][w]:
                    stack.append(w)
    # end 지점을 방문하였는지 반환
    return visit[end]
#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    #정점과 간선의 개수 입력
    V, E = map(int,input().split())
    arr = [[0] *(V+1) for _ in range(V+1)]
    #arr에 입력받은 연결된 정점 표시
    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1
    result = 1
    #입력받은 a가 b에 연결되어있는지 확인
    a, b= map(int,input().split())
    if not dfs(a,b):
        result = 0
    print('#{} {}'.format(tc, result))


