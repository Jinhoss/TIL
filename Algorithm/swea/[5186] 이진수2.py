# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = float(input())
    result = ''
    check = False
    # 이진수 변환할 때 2로 나누어서 진행했다면
    # 지수가 음수인 경우에는 0.5를 나누는 과정 즉 2를 곱하면서 확인하면 된다.
    while len(result) <= 11:
        n *= 2
        # 2를 곱하여서 1 이상이 되는 경우 '1'을 추가한다.
        if n >= 1:
            n-=1
            result += '1'
        # 2를 곱해도 1을 넘지 못하는 경우 '0'을 추가
        else:
            result += '0'
        # 변환이 끝났는지 체크
        if n == 0:
            check = True
            break
    if check:
        print('#{} {}'.format(tc, result))
    else:
        print('#{} overflow'.format(tc))