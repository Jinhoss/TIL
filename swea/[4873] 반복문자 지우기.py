#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    sen = input()
    lst=[]
    #문장을 돌며 이전에 담긴 문자와 담으려고 하는 문자가 같다면 제거해준다.
    for s in sen:
        if lst and s == lst[-1]:
            lst.pop()
        else:
            lst.append(s)
    print('#{}'.format(tc), len(lst))