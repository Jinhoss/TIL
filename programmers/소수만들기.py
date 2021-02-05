import itertools

def prime(x): #소수판별
    for m in range(2,x):
        if x%m==0:
            return False
    return True
    

# 리스트 중 3
def solution(nums): 
    answer=0
    n=list(itertools.combinations(nums,3))
    for i in n:
        if prime(sum(i)):
            answer+=1
    return answer