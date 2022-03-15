def check(result):
    for x,y,a in result:
        if a==0:
            if y!=0 and (x,y-1,0) not in result and (x-1,y,1) not in result and (x,y,1) \
            not in result:
                return True
        else:
            if (x, y-1, 0) not in result and (x+1, y-1, 0) not in result and \
        not ((x-1, y, 1) in result and (x+1, y, 1) in result):
                return True
    return False



def solution(n, build_frame):
    result=set()
    for x,y,a,build in build_frame:
        item=(x,y,a)
        if build:
            result.add(item)
            if check(result):
                result.remove(item)
        elif item in result:
            result.remove(item)
            if check(result):
                result.add(item)
    answer=map(list,result)
    return sorted(answer,key=lambda x:(x[0],x[1],x[2]))