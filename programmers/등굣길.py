def solution(m, n, puddles):
    matrix=[[0]*(m+1) for j in range(n+1)]
    matrix[1][1]=1
    for i in range(n+1):
        for j in range(m+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles:
                matrix[i][j]=0
            else:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
    
    return matrix[n][m]%1000000007