def solution(cap, n, deliveries, pickups):
    answer = 0

    deli_cnt = 0
    pick_cnt = 0

    for i in range(n-1, -1, -1):
        deli_cnt += deliveries[i]
        pick_cnt += pickups[i]

        while deli_cnt > 0 or pick_cnt > 0:
            deli_cnt -= cap
            pick_cnt -= cap
            answer += (i+1) * 2

    return answer