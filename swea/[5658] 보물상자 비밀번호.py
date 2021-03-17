import sys
sys.stdin = open('input.txt')

T = int(input())
change = {'A':10, 'B': 11, 'C':12, 'D':13, 'E':14, 'F':15}
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    lst = input()
    l = n//4
    number = set()
    for _ in range(l):
        for i in range(0, n + 1-l, l):
            number.add(lst[i: i+l])
        lst = lst[-1] + lst[:-1]
    word = sorted(number, reverse = True)[k-1]
    answer = 0
    for idx in range(l-1, -1, -1):
        if '0'<= word[idx] <='9':
            answer+=int(word[idx])*(16**(l-idx-1))
        else:
            answer+=change[word[idx]]*(16**(l-idx-1))
    print('#{} {}'.format(tc, answer))

