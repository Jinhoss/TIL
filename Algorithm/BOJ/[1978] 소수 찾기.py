prime_lst = [False] * 2 + [True] * 999
for i in range(2, 1001):
    if prime_lst[i]:
        for idx in range(2 * i, 1001, i):
            prime_lst[idx] = False
cnt = 0
N = int(input())
lst = list(map(int, input().split()))
for x in lst:
    if prime_lst[x]:
        cnt += 1
print(cnt)