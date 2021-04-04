import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[100000*100000] * (n) for _ in range(n)]
for _ in range(m):
    v, e, cost = map(int, input().split())
    if cost < arr[v-1][e-1]:
        arr[v - 1][e - 1] = cost
for path in range(n):
    for start in range(n):
        for end in range(n):
            if start == end:
                arr[start][end] = 0
            elif arr[start][end] > arr[start][path] + arr[path][end]:
                arr[start][end] = arr[start][path] + arr[path][end]

for start in range(n):
    for end in range(n):
        if arr[start][end] == 100000*100000:
            arr[start][end] = 0
for lst in arr:
    print(*lst)

