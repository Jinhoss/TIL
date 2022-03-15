def next(b, m, n):
    new = [lst[:] for lst in b]
    result = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if b[i][j] == -1:
                continue
            if b[i][j] == b[i + 1][j + 1] == b[i + 1][j] == b[i][j + 1]:
                new[i][j], new[i + 1][j], new[i + 1][j + 1], new[i][j + 1] = 0, 0, 0, 0

    for idx, val in enumerate(new):
        cnt = val.count(0)
        result += cnt
        new[idx] = [-1] * cnt + [a for a in val if a != 0]
    return new, result


def solution(m, n, board):
    answer = 0
    b = list(map(list, zip(*board)))
    while True:
        b, result = next(b, m, n)
        if result == 0:
            return answer
        answer += result