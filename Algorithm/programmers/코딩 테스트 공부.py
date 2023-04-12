def solution(alp, cop, problems):
    target_i, target_j = alp, cop
    for problem in problems:
        req_i, req_j = problem[:2]
        if req_i>=target_i:
            target_i = req_i
        if req_j>=target_j:
            target_j = req_j
    dp = [[300] * (target_j+1) for _ in range(target_i + 1)]
    dp[alp][cop] = 0
    for i in range(alp, target_i + 1):
        for j in range(cop, target_j + 1):
            if j+1<=target_j:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            if i+1<=target_i:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            for problem in problems:
                req_i, req_j, di, dj, cost = problem
                if i>=req_i and j>=req_j:
                    ni, nj = min(target_i,i + di), min(target_j,j + dj)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + cost)
    return dp[-1][-1]
    