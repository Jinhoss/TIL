from collections import deque

# 테스트케이스 & 인풋 입력
for tc in range(1, 11):
    input()
    # 큐 생성
    q = deque(list(map(int, input().split())))
    # 사이클 체크
    i = 0
    while True:
        x = q.popleft()
        # 큐에서 원소를 하나 뽑아 일정한 수를 뺀 뒤 다시 추가
        if i+1 < x:
            q.append(x-i-1)
            i = (i+1) % 5
        # 빼기 값이 양수가 아니라면 0을 추가하고 암호 완성
        else:
            q.append(0)
            break
    print('#{}'.format(tc), *q)