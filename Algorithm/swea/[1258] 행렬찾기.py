# import sys
# sys.stdin = open('input.txt')

T = int(input())

#행렬의 겉을 돌며 크기를 측정하는 함수
def matrix(x, y):
    #시작점
    si = x
    sj = y
    # 행, 열 개수 초기화
    row = 1
    column = 1
    while True:
        x += 1
        # 열 길이 체크
        if x < n  and arr[x][y] != 0 and visit[x][y] == False:
            row += 1
        else:
            x -= 1
            break
        # 행 길이 체크
    while True:
        y += 1
        if y < n and arr[x][y] and not visit[x][y]:
            column += 1
        else:
            y -= 1
            break
    for idx in range(si, x+1):
        for jdx in range(sj, y+1):
            visit[idx][jdx] = True

    return [row, column]
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            # 0이 아닌 값 & 방문하지 않은 지점이면 돌면서 행렬 크기를 측정한다.
            if arr[i][j] and not visit[i][j]:
                result.append(matrix(i, j))
    # 행렬의 크기를 첫 번재, 같은 사이즈라면 행의 크기를 기준으로 정렬
    result = sorted(result, key = lambda x: (x[0]*x[1],x[0]))
    print('#{} {}'.format(tc, len(result)), end=' ')
    for lst in result[:-1]:
        print(*lst, end = ' ')
    print(*result[-1])