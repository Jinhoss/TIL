# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    stack = []
    lst = list(input().split())
    result=0
    error=0
    for s in lst:
        if s=='.':
            result=stack.pop()
            break
        if s.isdigit():
            stack.append(s)
        else:
            if len(stack)>=2:
                x1 = int(stack.pop())
                x2 = int(stack.pop())
                if s=='+':
                    stack.append(x1 + x2)
                elif s=='-':
                    stack.append(x2 - x1)
                elif s=='*':
                    stack.append(x1*x2)
                elif s=='/':
                    stack.append(x2//x1)
            else:
                error=1
                break
    if error or len(stack):
        print('#{} error'.format(tc))
    else:
        print('#{} {}'.format(tc,result))




