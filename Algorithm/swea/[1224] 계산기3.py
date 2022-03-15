# import sys
# sys.stdin = open('input.txt')
#우선순위 계산
#괄호에 가장 낮은 우선순위 부여
def prior(s):
    if s=='*':
        return 2
    elif s == '+':
        return 1

    else:
        return 0
#테스트케이스 수 입력
for tc in range(1, 11):
    input()
    lst = list(input())
    stack = []
    string = ''
    #중위 표기 => 후위 표기 변경
    for s in lst:
        if s.isdigit():
            string += s
        # 여는 괄호인 경우 & 스택이 비어있는 경우 & 스택탑이 여는 괄호인 경우, 스택에 push
        elif s == '(' or not stack or stack[-1] == '(':
            stack.append(s)
        # 들어온 연산자가 스택의 연산자보다 우선순위가 높다면 스택에 push
        elif prior(s) > prior(stack[-1]) and s != ')':
            stack.append(s)
        else:
            # 스택이 비지않거나 들어온 연산자의 우선 순위가 스택의 탑보다 같거나 작은 경우에 반복
            while stack and prior(s) <= prior(stack[-1]):
                # 닫는 괄호라면 괄호없애고 정지한다.
                if stack[-1] == '(':
                    stack.pop()
                    break
                # 위의 조건에 해당하지 않는다면 결과 스택에 추가한다.
                string+=stack.pop()
            # 반복이 끝난후 닫는괄호가 아닐때만 스택에 push
            if s != ')':
                stack.append(s)
    # 남은 연산 저장
    while stack:
        operator = stack.pop()
        if operator != '(':
            string+=operator
    #후위표기식 계산
    for x in string:
        if x.isdigit():
            stack.append(x)
        elif x == '+':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(int(x1) + int(x2))
        elif x == '*':
            x1 = stack.pop()
            x2 = stack.pop()
            stack.append(int(x1) * int(x2))
    print('#{} {}'.format(tc, stack.pop()))