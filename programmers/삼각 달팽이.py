from itertools import chain
def turn(y,x,d):
    coordinate={'U':(-1,-1),'D':(1,0),'R':(0,1)}
    dy, dx= coordinate[d][0],coordinate[d][1]
    next_y,next_x=y+dy,x+dx
    return next_y,next_x

def check(next_y,next_x,n,snail):
    return next_y<0 or next_y>=n or next_x>next_y or snail[next_y][next_x]!=0

def solution(n):
    Next={'U':'D','D':'R','R':'U'}
    N=sum(range(1,n+1))
    snail=[[0]*i for i in range(1,n+1)]
    y,x,d=0,0,'D'
    for num in range(1,N+1):
        snail[y][x]=num
        if check(*turn(y,x,d),n,snail):
            d=Next[d]
        y,x=turn(y,x,d)
    return list(chain(*snail))