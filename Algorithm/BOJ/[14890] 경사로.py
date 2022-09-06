import sys

sys.stdin = open('input.txt')


def check(lst, N, L):
    visit = [False] * N
    for j in range(N - 1):
        base = lst[j]
        if lst[j+1] == base:
            continue
        else:
            flag1 = True
            for l in range(1, L+1):
                if j+l < N and not visit[j+l] and base - lst[j+l] == 1:
                    continue
                else:
                    flag1 = False
                    break
            if not flag1:
                flag2 = True
                if lst[j+1] - base == 1:
                    for l in range(L):
                        if j-l>=0 and not visit[j-l] and lst[j-l]==base:
                            continue
                        else:
                            flag2 = False
                            break
                else:
                    flag2 = False
            if flag1:
                for l in range(1, L+1):
                    visit[j+l] = True
            elif flag2:
                for l in range(L):
                    visit[j-l] = True
            else:
                return 0
    return 1


N, L = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))
cnt = 0
arr2 = [list(x) for x in zip(*arr)]
for lst in arr:
    cnt += check(lst, N, L)

for lst in arr2:
    cnt += check(lst, N, L)
print(cnt)

# print(check([3, 3, 2, 1, 1, 1], 6, 2))