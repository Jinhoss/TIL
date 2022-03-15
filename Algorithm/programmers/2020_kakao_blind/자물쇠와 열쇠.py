def attach(x,y,M,key,board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j]+=key[i][j]
def detach(x,y,M,key,board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j]-=key[i][j]
def rotation(arr):
    return list(zip(*arr[::-1]))

def check(board,M,N):
    for i in range(N):
        for j in range(N):
            if board[i+M][j+M]!=1:
                return False
    return True
    

def solution(key, lock):
    M=len(key)
    N=len(lock)
    board=[[0]*(M*2+N) for _ in range(M*2+N)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j]=lock[i][j]
    rotakey=key
    for _ in range(4):
        rotakey=rotation(rotakey)
        for x in range(1,M+N):
            for y in range(1,M+N):
                attach(x,y,M,rotakey,board)
                if check(board,M,N):
                    return True
                detach(x,y,M,rotakey,board)
    return False