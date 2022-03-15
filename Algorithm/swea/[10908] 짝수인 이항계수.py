# import sys
# sys.stdin = open('input.txt')

def pow(a, n):
    if n == 0:
        return 1
    else:
        return a * pow(a, n - 1)


T = int(input())
ans = []
for test_case in range(T):
    N = int(input())
    M, cnt = N, 0

    while N >= 1:
        if N % 2:
            cnt += 1
        N //= 2
    ans.append(M + 1 - int(pow(2, cnt)))
for i in range(T):
    print("#{} {}".format(i + 1, ans[i]))