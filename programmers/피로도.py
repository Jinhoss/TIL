def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if not visit[j] and k >= dungeons[j][0] and k >= dungeons[j][1]:
            visit[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visit[j] = 0


def solution(k, dungeons):
    global N, visit, answer
    answer = 0
    N = len(dungeons)
    visit = [0] * N
    dfs(k, 0, dungeons)
    return answer