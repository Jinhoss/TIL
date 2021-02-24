#우선순위 계산
def prior(s):
    if s=='*':
        return 2
    else:
        return 1
#테스트 케이스 수 입력
for tc in range(1,11):
    N = int(input())
    sentence = input()
    string=''
    stack = []
    #후위표기식으로 변경
    for s in sentence:
        #숫자는 바로 저장
        if s.isdigit():
            string+=s
        #숫자가 아닌 경우 & 스택이 비어 있지 않은 경우에 입력값과 stack의 top값 각각 우선순위를 비교한다.
        #입력값의 우선순위가 top의 우선순위보다 같거나 작은 경우에는 stack.pop()을 저장한다.
        else:
            while stack and (prior(s) <= prior(stack[-1])):
                string+=stack.pop()
            #스택이 비었다면 바로 push
            stack.append(s)
    #문자열을 다 돌고 남은 연산을 저장
    while stack:
        string+=stack.pop()
    #후위표기식 계산
    for x in string:
        if x.isdigit():
            stack.append(x)
        elif x=='+':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(int(x1)+int(x2))
        elif x=='*':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(int(x1)*int(x2))
    print('#{} {}'.format(tc, stack.pop()))
