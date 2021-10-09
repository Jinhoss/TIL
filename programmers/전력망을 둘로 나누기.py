def solution(n, wires):
    graph = {}
    for v1, v2 in wires:
        graph[v1] = graph.get(v1, []) + [v2]
        graph[v2] = graph.get(v2, []) + [v1]
    res = 100
    for v1, v2 in wires:
        visit = [False] * (n + 1)
        visit[v2] = True
        cnt = 0
        stack = [v1]
        while stack:
            cur = stack.pop()
            if not visit[cur]:
                stack+=graph[cur]
                visit[cur] = True
                cnt += 1 
        res = min(res, abs(n - 2 * cnt))
    return res