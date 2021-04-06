import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    cnt = 1
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]
    people.sort()
    max_v = people[0][1]

    for i in range(1, N):
        if max_v > people[i][1]:
            cnt += 1
            max_v = people[i][1]

    print(cnt)