import sys
input = sys.stdin.readline

n = int(input())

check = set()

for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            l = n - i - j - k
            num = i * 1 + j * 5 + k * 10 + l * 50
            check.add(num)
print(len(check))