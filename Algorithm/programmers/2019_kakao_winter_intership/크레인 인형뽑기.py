def solution(board, moves):
    
    col=[]
    result=0
    for move in moves:
        for n in range(len(board)):
            if board[n][move-1]:
                col.append(board[n][move-1])
                board[n][move-1]=0
                
                if len(col)>1 and col[-1]==col[-2]:
                    del col[-2:]
                    result+=2
                break
            
                
    return result