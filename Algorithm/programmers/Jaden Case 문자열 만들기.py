def solution(s):
    sp=s.split(" ")
    answer=""
    for i in sp:
        i=i.capitalize()
        if answer=="":
            answer=i
        else:
            answer=answer+" "+i
    return answer