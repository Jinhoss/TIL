import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

adj = [[] for _ in range(N)]
parties = []
know = list(map(int, sys.stdin.readline().split(" ")))
heard = [0 for _ in range(N)]

if know[0] == 0:
    print(M)
else:
    know.pop(0)
    for _ in range(M):
        party = list(map(int, sys.stdin.readline().split(" ")))
        if party[0] == 0:
            parties.append(["none"])
        else:
            parties.append(party[1:])
            if party[0] != 1:
                com = combinations(party[1:], 2)
                for each in com:
                    adj[each[0]-1].append(each[1] - 1)
                    adj[each[1]-1].append(each[0] - 1)

    queue = deque()
    for each in know:
        queue.append(each-1)
        heard[each-1] = 1

    while queue:
        now = queue.popleft()
        for one in adj[now]:
            if heard[one] == 0:
                heard[one] = 1
                queue.append(one)

    heardperson = []
    for i in range(len(heard)):
        if heard[i] == 1:
            heardperson.append(i+1)

    count = 0
    for party in parties:
        flag = 0
        for each in heardperson:
            if each in party:
                flag = 1
                break
        if flag == 0:
            count += 1

    print(count)