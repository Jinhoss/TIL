# import sys
# sys.stdin = open('input.txt')

def sol(arr, visit, test, r, c):
    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    stack = [[0, 0, 3, 0]]
    while stack:
        x, y, d, m = stack.pop()
        if visit[x][y][d][m] == test:
            continue
        else:
            visit[x][y][d][m] = test
            if arr[x][y] == '<' or (arr[x][y] == '_' and m != 0):
                dx, dy = delta[1]
                stack.append([(x + dx) % r, (y + dy) % c, 1, m])
            elif arr[x][y] == '>' or (arr[x][y] == '_' and m == 0):
                dx, dy = delta[3]
                stack.append([(x + dx) % r, (y + dy) % c, 3, m])
            elif arr[x][y] == '^' or (arr[x][y] == '|' and m != 0):
                dx, dy = delta[0]
                stack.append([(x + dx) % r, (y + dy) % c, 0, m])
            elif arr[x][y] == 'v' or (arr[x][y] == '|' and m == 0):
                dx, dy = delta[2]
                stack.append([(x + dx) % r, (y + dy) % c, 2, m])
            elif arr[x][y] == '@':
                return True
            elif arr[x][y] == '+':
                dx, dy = delta[d]
                stack.append([(x + dx) % r, (y + dy) % c, d, (m + 1) % 16])
            elif arr[x][y] == '-':
                dx, dy = delta[d]
                stack.append([(x + dx) % r, (y + dy) % c, d, (m - 1) % 16])
            elif arr[x][y] == '.':
                dx, dy = delta[d]
                stack.append([(x + dx) % r, (y + dy) % c, d, m])
            elif arr[x][y] == '?':
                for i in range(4):
                    dx, dy = delta[i]
                    stack.append([(x + dx) % r, (y + dy) % c, i, m])
            else:
                dx, dy = delta[d]
                stack.append([(x + dx) % r, (y + dy) % c, d, int(arr[x][y])])
    return False

T = int(input())
visit = [[[[0 for _ in range(16)] for _ in range(4)] for _ in range(20)] for _ in range(20)]
for tc in range(1, T+1):
    r, c = map(int, input().split())
    arr = [input() for _ in range(r)]
    answer = sol(arr, visit, tc, r, c)
    if answer == True:
        answer = 'YES'
    else:
        answer = 'NO'
    print('#{} {}'.format(tc, answer))