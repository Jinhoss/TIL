# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house_lst = []
    #집의 위치를 기록
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house_lst.append((i, j))
    result = 1
    # k 범위를 조정해가며 최대 값을 찾는다.
    for k in range(2, N + 2):
        for i in range(N):
            for j in range(N):
                cnt = 0
                for x, y in house_lst:
                    # 범위 내에 존재한다면 count 값을 증가
                    if abs(x-i) + abs(y-j) < k:
                        cnt+=1
                # 기존의 최대값보다 크며, 손해를 보지 않으면(이익 - 비용 >=0) 최대값 갱신
                if cnt > result and cnt * M >= k**2 + (k-1)**2:
                    result = cnt
    print('#{} {}'.format(tc, result))