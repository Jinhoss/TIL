from collections import deque

def check(cur1, cur2, new_board):
    cand = []
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in delta:
        nxt1 = (cur1[0] + dx, cur1[1] + dy)
        nxt2 = (cur2[0] + dx, cur2[1] + dy)
        if not new_board[nxt1[0]][nxt1[1]] and not new_board[nxt2[0]][nxt2[1]]:
            cand.append((nxt1, nxt2))
            
    delta2 = [-1, 1]
    if cur1[0] == cur2[0]:
        for d in delta2:
            if not new_board[cur1[0]+d][cur1[1]] and not new_board[cur2[0]+d][cur2[1]]:
                cand.append((cur1, (cur1[0]+d, cur1[1])))
                cand.append((cur2, (cur2[0]+d, cur2[1])))
    else:
        for d in delta2:
            if not new_board[cur1[0]][cur1[1] + d] and not new_board[cur2[0]][cur2[1] + d]:
                cand.append((cur1, (cur1[0], cur1[1] + d)))
                cand.append((cur2, (cur2[0], cur2[1] + d)))
    return cand

def solution(board):
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]
    q = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])
    
    while q:
        cur1, cur2, count = q.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for nxt in check(cur1, cur2, new_board):
            if nxt not in confirm:
                q.append((*nxt, count+1))
                confirm.add(nxt)