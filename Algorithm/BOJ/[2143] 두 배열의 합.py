T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dic = {}
for i in range(n):
    for j in range(i, n):
        sum_a = sum(A[i: j + 1])
        dic[sum_a]  = dic.get(sum_a, 0) + 1

ans = 0
for i in range(m):
    for j in range(i, m):
        ans += dic.get(T - sum(B[i: j + 1]), 0)

print(ans)