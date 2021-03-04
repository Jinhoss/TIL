from collections import deque
# import sys
# sys.stdin = open('input.txt')
# 테스트케이스 입력
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # 피자의 원소가 몇 번째 원소인지를 함께 저장한다.
    pizza = deque(enumerate(list(map(int,input().split())), 1))
    oven = deque()
    # 오븐 최대 용량까지 피자를 넣어준다.
    for _ in range(n):
        oven.append(pizza.popleft())
    # 피자가 한개가 남을 때까지 진행
    while len(oven) > 1:
        # 공간이 비었는데 피자가 아직 남아있다면 추가해준다.
        if len(oven) < n and pizza:
            oven.append(pizza.popleft())
        idx, c = oven.popleft()
        # 치즈 양이 0 이라면 제거해준다.
        if not c//2:
            continue
        # 치즈가 남아있다면 뒤에 추가해준다.
        else:
            oven.append((idx, c//2))
    print('#{} {}'.format(tc, oven.popleft()[0]))
