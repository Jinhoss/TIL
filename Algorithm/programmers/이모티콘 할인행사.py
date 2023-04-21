from collections import deque


def cal(users, emoticons, dis_lst):
    l = len(emoticons)
    dis_v = [0.9, 0.8, 0.7, 0.6]
    total_price = 0
    member = 0
    for d_limit, p_limit in users:
        price = 0
        for idx in range(l):
            if dis_lst[idx] >= d_limit:
                price += ((100-dis_lst[idx]) * emoticons[idx])//100
        if price >= p_limit:
            member += 1
        else:
            total_price += price

    return total_price, member


def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    q = deque()
    q.append((0, []))
    l = len(emoticons)
    result = []
    while q:
        idx, lst = q.popleft()
        if idx == l:
            profit, member = cal(users, emoticons, lst)
            result.append((member, profit))
            continue
        for i in range(4):
            dis = discount[i]
            new_lst = [x for x in lst]
            new_lst.append(dis)
            q.append((idx + 1, new_lst))

    answer = sorted(result, key=lambda x: (-x[0], -x[1]))
    return answer[0]