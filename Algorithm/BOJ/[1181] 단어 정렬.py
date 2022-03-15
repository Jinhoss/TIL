n = int(input())
lst = []
for _ in range(n):
    x = input().rstrip()
    if x not in lst:
        lst.append(x)
lst.sort(key = lambda x: (len(x), x))
for idx in range(len(lst)):
    print(lst[idx])