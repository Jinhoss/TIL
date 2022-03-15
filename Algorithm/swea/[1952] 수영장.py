# import sys
# sys.stdin = open('input.txt')

# dp로 구현하였다.
T = int(input())
for tc in range(1, T + 1):
    # 각 티켓의 요금
    tickets = list(map(int, input().split()))
    # 월별 수영장 이용 계획
    plans = list(map(int, input().split()))
    # 3개월 권을 식에 표현하고 싶어 2월까지는 대입하였다.
    dp = [0]*12
    dp[0] = min(tickets[0] * plans[0], tickets[1])
    dp[1] = dp[0] + min(tickets[0] * plans[1], tickets[1])
    dp[2] = min(dp[1] + min(tickets[0] * plans[2], tickets[1]), tickets[2])
    # 3개월권을 이용하는 것, 일일 이용권을 이용하는 것, 1개월 이용권을 이용하는 것 중 가장 효율이 높은 것을 저장한다.
    for i in range(3, 12):
        dp[i] = min(dp[i-3] + tickets[2], dp[i-1] + min(tickets[0] * plans[i], tickets[1]))
    # 12월까지 모두 돌고나서 1년 이용권을 이용하는 것과 비교하여 결과값을 도출한다.
    dp[-1] = min(dp[-1], tickets[3])
    print('#{} {}'.format(tc, dp[-1]))
