import sys
input = sys.stdin.readline

# 카탈린 수로 구현
T = int(input())
# factorial 함수
def factirial(n):
    if n == 1 or n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result*=i
        return result

for _ in range(T):
    n = int(input())
    # 홀수인 경우에는 올바른 괄호가 될 수 없다.
    if n%2:
        print(0)
    # 짝수인 경우에는 C(n, n//2) - C(n, n//2-1) 값이 문제에서 요구하는 답이 된다.
    else:
        answer = factirial(n)//(factirial(n//2)**2) - factirial(n)//(factirial(n//2 + 1) * factirial(n//2 - 1))
        print(answer%1000000007)