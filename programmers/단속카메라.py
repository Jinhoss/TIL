def solution(routes):
    routes=sorted(routes,key=lambda x: x[1])
    n=len(routes)
    lst=[False]*n
    answer=0
    for i in range(n):
        if lst[i]:
            continue
        camera=routes[i][1]
        answer+=1
        for j in range(n):
            if (routes[j][0]<=camera)&(routes[j][1]>=camera):
                lst[j]=True
    return answer