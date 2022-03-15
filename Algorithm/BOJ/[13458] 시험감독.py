N = int(input())
A_lst = list(map(int, input().split()))

B, C = map(int, input().split())

result = 0
for A in A_lst:
    result += 1
    target = max(A - B, 0)
    q, r = divmod(target, C)
    if q >0 and r == 0:
        result += q
    elif q==0 and r>0:
        result += 1
    elif q==0 and r==0:
        continue
    else:
        result += q + 1

print(result)
