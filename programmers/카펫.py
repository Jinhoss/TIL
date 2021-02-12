def solution(brown, yellow):
    t=brown+yellow
    j=3
    i=t//3
    while j<=brown:
        if ((i+j)*2-4)==brown and i*j==t:
            answer=[i,j]
            break
        else:
            j+=1
            i=t//j
        
        
    return answer