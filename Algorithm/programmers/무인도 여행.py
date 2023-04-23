
def solution(maps):
    r = len(maps)
    c  = len(maps[0])
    visit = [[False] * c for _ in range(r)]
    def cal(x, y):
        d_lst = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit[x][y] = True
        stack = []
        result = int(maps[x][y])
        stack.append((x, y))
        while stack:
            cx, cy = stack.pop()
            for dx, dy in d_lst:
                nx, ny = cx + dx, cy + dy
                if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and maps[nx][ny]!='X':
                    visit[nx][ny] = True
                    stack.append((nx, ny))
                    result += int(maps[nx][ny])
        return result
    
    
    answer = []
    for i in range(r):
        for j in range(c):
            if maps[i][j]!='X' and not visit[i][j]:
                v = cal(i, j)
                answer.append(v)
    if not answer:
        return [-1]
    else:
        return sorted(answer)
                