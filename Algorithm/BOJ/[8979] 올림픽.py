import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

country_lst = []
N, K = map(int, input().split())
gold, silver, bronze = 0, 0, 0
for _ in range(N):
    country = list(map(int, input().split()))
    if country[0] == K:
        gold, silver, bronze = country[1], country[2], country[3]
    else:
        country_lst.append(country[1:])

rank = 1

while country_lst:
    g, s, b = country_lst.pop()
    if gold > g:
        continue
    elif gold == g:
        if silver > s:
            continue
        elif silver == s:
            if bronze > b:
                continue
            elif bronze == b:
                continue
            else:
                rank+=1
        else:
            rank+=1
    else:
        rank+=1

print(rank)

