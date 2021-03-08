# import sys
# sys.stdin = open('input.txt')

# 계단이 1개 or 2개인 경우를 고려하지 못해 오래걸림..

n = int(input())
stairs = [int(input()) for _ in range(n)]
score = [0] * (n+1)
score[1] = stairs[0]
if n>1:
    score[2] = stairs[0] + stairs[1]
# 계단이 두 개 이상일 때, 현재 idx 계단에 도달하는 방법은 두 가지가 있다.
if n>2:
    for idx in range(1, n-1):
        score[idx + 2] = max(stairs[idx] + score[idx-1], score[idx])+stairs[idx + 1]
print(score[n])