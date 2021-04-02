N, score, P = map(int, input().split())

if N == 0:
    print(1)

else:
    lst = list(map(int, input().split())) + [0] * (P - N)
    if N == P and lst[-1] >= score:
        print(-1)
    else:
        rank = N + 1
        for i in range(N):
            if lst[i] <= score:
                res = i + 1
                break
        print(rank)