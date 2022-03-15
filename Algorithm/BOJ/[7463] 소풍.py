import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())

cnt = 1
while cnt < N:
    if K % (N - cnt + 1) == 0:
        x = N - cnt + 1
    else:
        x = K % (N - cnt + 1)
    if x == M or cnt== N:
        break
    else:
        if M > x:
            M -= x
        else:
            M = N - cnt + M - x + 1
    cnt+=1
print(cnt)
