from collections import deque

# bfs방식으로 수빈과 동생을 동시에 움직이며 만나는지 확인 => 시간초과 발생
# 시간초과 => x + 1, x - 1로 인해 같은 위치를 반복적으로 계속 들러 시간이 낭비됨
# 수빈이 움직일 수 있는 위치를 모두 탐색한 이후에
# 동생이 그 위치에 갈 수 있는지에 대한 여부를 확인
N, K = map(int, input().split())
q = deque()
q.append((N, 0))
result = -1
# x + 1, x - 1로 인해 짝수 시간, 홀수 시간으로 나누어서 저장
visit = [[-1] * 500001 for _ in range(2)]
visit[0][N] = 0
while q:
    x, time = q.popleft()
    for nx in (x * 2, x + 1, x - 1):
        if 0 <= nx <= 500000 and time%2 and visit[0][nx] == -1:
            visit[0][nx] = time + 1
            q.append((nx, time + 1))
        elif 0<= nx <= 500000 and not time%2 and visit[1][nx] == -1:
            visit[1][nx] = time + 1
            q.append((nx, time + 1))
time = 0
result = -1
while K <= 500000:
    # 저장된 값이 time보다 작기만하면 수빈이 x + 1, x -1을 반복하며
    # 시간을 조절할 수 있기 때문에 만날 수 있다.
    if visit[time%2][K] != -1 and visit[time%2][K] <= time:
        result = time
        break
    time +=1
    K += time

print(result)