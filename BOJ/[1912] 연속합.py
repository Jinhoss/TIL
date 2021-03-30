N = int(input())
lst = list(map(int, input().split()))
check = [-1000] * N
check[0] = lst[0]
max_v = lst[0]
for i in range(1, N):
    if check[i-1]>0:
        check[i] = lst[i] + check[i-1]
    else:
        check[i] = lst[i]
    if check[i] > max_v:
        max_v = check[i]
print(max_v)