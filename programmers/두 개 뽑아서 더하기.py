from itertools import combinations
def solution(numbers):
    x=list(combinations(numbers,2))
    result=[]
    for i in x:
        if (i[0]+i[1]) not in result:
            result.append((i[0]+i[1]))
    result=sorted(result)
    return result