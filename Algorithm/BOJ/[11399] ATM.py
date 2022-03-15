n = int(input())
lst = list(map(int,input().split()))
lst.sort()
answer=0
for i in range(n):
    answer += (n-i) * lst[i]
print(answer)