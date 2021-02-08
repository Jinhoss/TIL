def solution(array, commands):
    answer = []
    for i in commands:
        n=int(i[0])-1
        m=int(i[1])
        x=array[n:m]
        answer.append(sorted(x)[i[2]-1])
    return answer