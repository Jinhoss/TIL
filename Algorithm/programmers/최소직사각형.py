def solution(sizes):
    w = []
    h = []
    for i, j in sizes:
        if i > j:
            w.append(i)
            h.append(j)
        else:
            h.append(i)
            w.append(j)
    answer = max(w) * max(h)
    return answer