def solution(board):
    x=len(board[0])
    y=len(board)
    for i in range(1,y):
        for j in range(1,x):
            if board[i][j]==1:
                board[i][j]=min(board[i-1][j-1],board[i][j-1],board[i-1][j])+1
    return max([ans for row in board for ans in row])**2