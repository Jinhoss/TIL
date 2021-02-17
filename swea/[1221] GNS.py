# import sys
# sys.stdin=open("gns_input.txt")

T = int(input())
for tc in range(1, T+1):
    x=input()
    lst = list(input().split())
    num_dic={"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for i in lst:
        num_dic[i]+=1
    result=''
    for key, value in num_dic.items():
        temp = ' '.join([key] * value)
        result += temp + ' '
    print('#%d'%tc)
    print(result)

