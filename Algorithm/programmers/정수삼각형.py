def solution(triangle):
    l=len(triangle)
    for row in range(1,l):
        for i in range(len(triangle[row])):
            if i==0:
                triangle[row][i]+=triangle[row-1][i]
            elif i==len(triangle[row])-1:
                triangle[row][i]+=triangle[row-1][-1]
            else:
                triangle[row][i]+=max(triangle[row-1][i-1],triangle[row-1][i])
    return max(triangle[-1])