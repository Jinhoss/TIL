def solution(weights, head2head):
    l = len(weights)
    info_lst = []
    for i in range(l):
        total_count = 0
        win_count = 0
        heavy_count = 0
        info = head2head[i]
        for j in range(l):
            if info[j] == 'N':
                continue
            elif info[j] == 'W':
                win_count += 1
                total_count += 1
                if weights[i] <weights[j]:
                    heavy_count += 1
            else:
                total_count += 1
        if total_count == 0:
            win_rate = 0
        else:
            win_rate = win_count / total_count
        info_lst.append((win_rate, heavy_count, weights[i], i + 1))
    result = sorted(info_lst, key = lambda x: (-x[0], -x[1], -x[2]))
    
    return [num[-1] for num in result]
    