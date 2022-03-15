import sys
input = sys.stdin.readline

N = int(input())
W = []
INF = float('inf')
for _ in range(N):
    W.append(list(map(int, input().split())))
dp = [[None] * (1 << N) for _ in range(N)]

def find_path(last, visited):
    # 모두 방문한 경우
    if visited == (1 << N ) - 1:
        # 마지막 도시에서 출발지로 가는 경로가 있으면 반환하고
        # 없다면 INF를 반환하여 정답이 될 수 없게 한다.
        return W[last][0] or INF

    # 값이 존재한다면
    if dp[last][visited] is not None:
        # 값 반환
        return dp[last][visited]

    tmp = INF
    # 모든 도시를 순회
    for city in range(N):
        if visited & (1 << city) == 0 and W[last][city] != 0:
            tmp = min(tmp, find_path(city, visited|(1 << city)) + W[last][city])
    dp[last][visited] = tmp
    return tmp
print(find_path(0, 1))
