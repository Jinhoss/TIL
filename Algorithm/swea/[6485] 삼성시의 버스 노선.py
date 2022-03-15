#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
#버스 노선의 개수 입력
    N = int(input())
#버스 정류장을 지나는 노선의 개수를 세기 위해 0으로 초기화된 리스트 생성
    bus_stop = [0] * 5001
#버스 노선을 입력받아 버스 노선이 지나가는 버스 정류장들을 카운트
    for _ in range(N):
        a, b = map(int, input().split())
        for x in range(a, b + 1):
            bus_stop[x] += 1
    P = int(input())
#입력 받은 P의 수만큼 정류장 번호를 호출하면 지나간 횟수를 result에 담음
    result = []
    for _ in range(P):
        c = int(input())
        result.append(bus_stop[c])
    print('#{}'.format(tc), end=' ')
    print(*result)

