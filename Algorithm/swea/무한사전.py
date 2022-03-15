# ord(a)=97
# def check(s,t):
#     if not s:
#         if t:
#             return t=='a'
#         else:
#             return True
#     if s[0]==t[0]:
#         return check(s[0:],t[0:])
#     else:
#         if ord(t[0])-ord(s[0])>1:
#             return False
        
T=int(input())
for tc in range(1,T+1):
    p=input()
    q=input()
    cal=[]
    for i in range(len(p)):
        if (ord(q[i])-ord(p[i]))%26<=1:
            cal.append((ord(q[i])-ord(p[i]))%26)
            print(cal)
        else:
            print('#{} Y'.format(tc))
            break
    if len(q)==len(p):
            
    print(cal)
    # if check(p,q):
    #     print('#{} N'.format(tc))
    # else:
    #     print('#{} Y'.format(tc))


