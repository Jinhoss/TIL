N = int(input())
check = [0] * 41
lst = list(map(int, input().split()))

for n in lst:
    check[n] += 1

before = 2
result = False
for cnt in check:
    if cnt > before:
        result = True
        break
    before = cnt

if result:
    print(0)
else:
    print(1<<check.count(2) + (1 in check))