from itertools import permutations
def check(x,cand,s,b):
    strike=0
    for i in range(3):
        if x[i]==cand[i]:
            strike+=1
    if s!=strike:
        return False
    ball=len(set(x)&set(cand))-strike
    if ball!=b:
        return False
    return True
    

def solution(baseball):
    answer = 0
    lst=list(permutations([1,2,3,4],3))
    for i in baseball:
        for j in lst[:]:
            if not check([int(i) for i in list(str(i[0]))],j,i[1],i[2]):
                lst.remove(j)
    return len(lst)