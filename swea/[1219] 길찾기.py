# import sys
# sys.stdin = open("input.txt")

for _ in range(10):
    #테스트 케이스 넘버와 입력받는 간선의 개수
    tc, V = map(int, input().split())
    lst = list(map(int, input().split()))
    # 정점과 해당 정점에서 이동가능한 정점을 저장
    arr = {}
    for i in range(0, V*2, 2):
        v = lst[i]
        e= lst[i+1]
        arr[v] = arr.get(v, [])+ [e]
    #시작지점인 0부터 시작
    stack = []
    stack.append(0)
    visit = [0] * 100
    #갈 수 있는 정점들을 순회하며 방문기록 저장
    while stack:
        x = stack.pop()
        visit[x] = 1
        if x in arr.keys():
            for w in arr[x]:
                if not visit[w]:
                    stack.append(w)
#도착지점의 방문 여부 출력
    print('#{} {}'.format(tc, visit[-1]))

