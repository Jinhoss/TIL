def dfs(idx):
    global answer
    if idx == cnt:
        result = int(''.join(lst))
        if answer < result:
            answer = result
        return
    for i in range(len_lst):
        for j in range(i + 1, len_lst):
            lst[i], lst[j] = lst[j], lst[i]
            check = ''.join(lst)
            if not check in graph[idx + 1]:
                graph[idx + 1].append(check)
                dfs(idx + 1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T + 1):
    lst, cnt = input().split()
    lst = list(lst)
    cnt = int(cnt)
    len_lst = len(lst)
    graph = [[] for _ in range(cnt + 1)]
    answer = -1
    dfs(0)
    print('#{} {}'.format(tc, answer))
