# input 입력
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))
    # idx: 현재 위치, cnt: 충전횟수
    idx = 0
    cnt = 0
    # 충전한 위치에서 목표까지 도달할때까지 반복
    while idx + K < N:
        check = []
        # 현재 위치에서 갈 수 있는 거리 중 배터리가 있는 가장 먼 정류장을 선택
        for i in range(1, K + 1):
            if i + idx in battery:
                check.append(i)
        if check:
            idx += check[-1]
            cnt += 1
        # 충전을 하고 다음 위치의 충전소까지 도달 못한다면 break하고 0을 출력
        else:
            print('#{} 0'.format(tc))
            break
    if idx + K >= N:
        print('#{} {}'.format(tc, cnt))





