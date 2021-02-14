import re

def solution(s):
    lst=[]
    reList=re.sub('(\w{1})' ,'\g<1> ',s).split()
    for i in reList:
        if len(lst)==0:
            lst.append(i)
        else:
            if i==lst[-1]:
                lst.pop()
            else:
                lst.append(i)
    if len(lst)==0:
        return 1
    else:
        return 0