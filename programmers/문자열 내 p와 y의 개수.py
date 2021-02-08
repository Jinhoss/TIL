def solution(s):
    x=''.join(s)
    
    a=0
    b=0
    for i in x:
        if i=='p' or i=='P':
            a+=1
        elif i=='y' or i=='Y':
            b+=1
    if a==b:
        return True
    else:
        return False