import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = float('inf')

for path in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][path] + arr[path][j]:
                arr[i][j] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == float('inf'):
            arr[i][j] = 0
for lst in arr:
    print(*lst)