def solution(n):
    x=bin(n)[2:].count('1')
    m=n+1
    while x!=bin(m)[2:].count('1'):
        m+=1
    return m