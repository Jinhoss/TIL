def sol(x):
    return x * x
lst = list(map(int, input().split()))
print(sum(list(map(sol, lst)))%10)