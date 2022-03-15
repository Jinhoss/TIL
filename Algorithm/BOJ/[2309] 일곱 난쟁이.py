from collections import deque


q = deque()
lst = []

for _ in range(9):
    lst.append(int(input()))

q.append(([], 0, 0))

while q:
    height, idx, cnt = q.popleft()
    if 9 - idx + cnt <7:
        continue
    if cnt == 7 and sum(height) == 100:
        print(*sorted(height))
        break
    if idx == 9:
        continue
    height2 = height[:]
    q.append((height2, idx + 1, cnt))
    height3 = height[:]
    height3.append(lst[idx])
    q.append((height3, idx + 1, cnt + 1))

