from collections import deque
# 테스트케이스 입력
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    # 횟수 m번 회전
    while cnt < m :
        q.append(q.popleft())
        cnt += 1
    # 가장 앞에 있는 원소 출력
    print('#{} {}'.format(tc, q.popleft()))