#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    sentence = input()
    l = len(sentence)
    lst = []
    result=1
    for s in sentence:
        #( 이나 {이면 lst에 담음
        if s=='(' or s=='{':
            lst.append(s)
        #) 이나 }이 나오면 (나 { 전에 나왔는지 확인
        elif s==')' or s=='}':
            if len(lst)==0:
                result=0
                break
            #적절하게 짝이 이루어졌는지 확인
            elif s==')' and lst.pop() =='{':
                result=0
                break
            elif s=='}' and lst.pop() =='(':
                result=0
                break
    #괄호가 모두 짝이 맞게 닫혔는지 확인
    if len(lst):
        result=0

    print('#{} {}'.format(tc, result))

