# import sys
# sys.stdin = open('input.txt')

# 각 말이 목표지점까지 달리는데 필요한 시간을 측정한 후
# 가장 오래 걸린 시간을 기준으로 계산
T = int(input())
for tc in range(1, T + 1):
    D, N = map(int, input().split())
    max_time = 0
    for _ in range(N):
        K, S = map(int, input().split())
        # 각 말이 목표지점까지 달리는데 필요한 시간
        time = (D-K)/S
        # 시간의 최대값 저장
        if time > max_time:
            max_time = time
    # 시간의 최대값을 기준으로 속력을 정한다. 출력은 소수 7번째자리까지
    print('#%d %0.7f'%(tc, D/max_time))