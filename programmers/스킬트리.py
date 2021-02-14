def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        list=[]
        fin=True
        for j in i:
            if j in skill:
                list.append(j)
        for n in range(len(list)):
            if list[n]!=skill[n]:
                fin=False
                break
        if fin==True:
            answer+=1
                
    return answer