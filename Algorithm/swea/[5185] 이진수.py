# import sys
# sys.stdin = open('input.txt')

T = int(input())
# 16진수 변환
dic = {'A' : 10, 'B': 11, 'C':12, 'D':13, 'E':14, 'F':15}
for tc in range(1, T + 1):
    l, string = input().split()
    result = ''
    for i in range(int(l)):
        # 10 ~ 15인 경우
        if 'A' <= string[i] <='F':
            result += bin(dic[string[i]])[2:].zfill(4) # 각 숫자마다 네 자리를 채움
        # 9 이하인 경우
        else:
            result += bin(int(string[i]))[2:].zfill(4)

    print('#{} {}'.format(tc, result))
