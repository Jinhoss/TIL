import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[float('inf')] * n for _ in range(n)]


for _ in range(m):
    v, e = map(int, input().split())
    arr[v - 1][e - 1] = 1
    arr[e - 1][v - 1] = 1

for path in range(n):
    for s in range(n):
        for e in range(n):
            if s == e:
                arr[s][e] = 0
            elif arr[s][e] > arr[s][path] + arr[path][e]:
                arr[s][e] = arr[s][path] + arr[path][e]
min_v = float('inf')
result = 0
for idx in range(n):
    if sum(arr[idx]) < min_v:
        min_v = sum(arr[idx])
        result = idx + 1
print(result)
