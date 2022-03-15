N = int(input())
x = []
y = []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])
sum_v1, sum_v2 = 0, 0
for i in range(N):
    sum_v1 += x[i] * y[i + 1]
    sum_v2 += y[i] * x[i + 1]

print(abs(sum_v1 - sum_v2)/2)
